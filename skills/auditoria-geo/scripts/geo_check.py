#!/usr/bin/env python3
"""geo_check.py — recoge las señales GEO de una URL y devuelve JSON.

Uso:
    python3 geo_check.py https://ejemplo.es
    python3 geo_check.py --html portada.html --robots robots.txt [--base https://ejemplo.es]

Sin dependencias fuera de la librería estándar. No puntúa: solo recoge
evidencia. La interpretación está en references/senales-ia.md.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36 geo_check/1.0"
)
TIMEOUT = 20

# Bots de IA. Ver references/rastreadores.md. citacion=True son los que
# alimentan respuestas; el resto son de entrenamiento u otros usos.
AI_BOTS = {
    "GPTBot": {"proveedor": "OpenAI", "tipo": "entrenamiento", "citacion": False},
    "OAI-SearchBot": {"proveedor": "OpenAI", "tipo": "busqueda", "citacion": True},
    "ChatGPT-User": {"proveedor": "OpenAI", "tipo": "usuario", "citacion": True},
    "ClaudeBot": {"proveedor": "Anthropic", "tipo": "entrenamiento", "citacion": False},
    "Claude-SearchBot": {"proveedor": "Anthropic", "tipo": "busqueda", "citacion": True},
    "Claude-User": {"proveedor": "Anthropic", "tipo": "usuario", "citacion": True},
    "PerplexityBot": {"proveedor": "Perplexity", "tipo": "busqueda", "citacion": True},
    "Perplexity-User": {"proveedor": "Perplexity", "tipo": "usuario", "citacion": True},
    "Google-Extended": {"proveedor": "Google", "tipo": "entrenamiento/grounding Gemini", "citacion": False},
    "Googlebot": {"proveedor": "Google", "tipo": "busqueda (AI Overviews)", "citacion": True},
    "Bingbot": {"proveedor": "Microsoft", "tipo": "busqueda (Copilot)", "citacion": True},
    "Applebot": {"proveedor": "Apple", "tipo": "busqueda", "citacion": True},
    "Applebot-Extended": {"proveedor": "Apple", "tipo": "entrenamiento", "citacion": False},
    "meta-externalagent": {"proveedor": "Meta", "tipo": "entrenamiento", "citacion": False},
    "Amazonbot": {"proveedor": "Amazon", "tipo": "otros", "citacion": False},
    "DuckAssistBot": {"proveedor": "DuckDuckGo", "tipo": "busqueda", "citacion": True},
    "MistralAI-User": {"proveedor": "Mistral", "tipo": "usuario", "citacion": True},
    "CCBot": {"proveedor": "Common Crawl", "tipo": "entrenamiento", "citacion": False},
    "Bytespider": {"proveedor": "ByteDance", "tipo": "entrenamiento", "citacion": False},
}

# Firmas de CMS. Se comprueban en orden; gana la primera que coincide.
CMS_SIGNATURES = [
    ("WordPress", [r"/wp-content/", r"/wp-includes/", r'name="generator" content="WordPress']),
    ("Shopify", [r"cdn\.shopify\.com", r"Shopify\.theme", r"myshopify\.com"]),
    ("Wix", [r"static\.wixstatic\.com", r"wix\.com", r"X-Wix-"]),
    ("Squarespace", [r"static1\.squarespace\.com", r"squarespace\.com", r"sqs-"]),
    ("IONOS", [r"ionos\.(es|com)", r"1and1", r"mywebsite-editor", r"sitebuilder"]),
    ("Jimdo", [r"jimdo\.com", r"jimdosite", r"jimdo-"]),
    ("Webflow", [r"webflow\.com", r"data-wf-page"]),
    ("PrestaShop", [r"prestashop", r"/modules/ps_"]),
    ("Joomla", [r'name="generator" content="Joomla', r"/media/jui/"]),
    ("Drupal", [r'name="generator" content="Drupal', r"/sites/default/files"]),
    ("Next.js", [r"/_next/static/", r"__NEXT_DATA__"]),
    ("Nuxt", [r"/_nuxt/", r"__NUXT__"]),
    ("Duda", [r"cdn\.website-start\.de", r"dudamobile", r"_dm_"]),
    ("GoDaddy", [r"img1\.wsimg\.com", r"godaddy"]),
    ("HubSpot", [r"hs-scripts\.com", r"hubspot"]),
    ("Elementor", [r"elementor"]),  # constructor, no CMS; se reporta aparte
]

PHONE_RE = re.compile(r"(?<!\d)(?:\+34|0034)?[\s.-]?[6789]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ADDRESS_RE = re.compile(
    r"\b(?:C/|Calle|Avda\.?|Avenida|Plaza|Pza\.?|Paseo|Carretera|Ctra\.?|"
    r"Pol[ií]gono|Camino|Ronda|Travesía|Glorieta)\s+[^\n<>,]{3,60}?,?\s*(?:n[ºo°]?\s*)?\d{1,4}\b",
    re.IGNORECASE,
)
POSTAL_RE = re.compile(r"(?<!\d)(?:0[1-9]|[1-4]\d|5[0-2])\d{3}(?!\d)")
QUESTION_WORDS = ("qué", "que", "cómo", "como", "cuánto", "cuanto", "cuándo", "cuando",
                  "dónde", "donde", "por qué", "porque", "cuál", "cual", "quién", "quien",
                  "what", "how", "why", "when", "where", "which", "who")


class PageParser(HTMLParser):
    """Extrae texto visible, encabezados, JSON-LD, enlaces y metas."""

    SKIP = {"script", "style", "noscript", "template", "svg"}
    NOISE = {"nav", "footer", "header", "aside"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.text_parts = []
        self.headings = []  # (tag, text)
        self.jsonld_raw = []
        self.metas = {}
        self.title = ""
        self.tel_links = 0
        self.mailto_links = 0
        self.time_tags = []
        self._current_heading = None
        self._in_jsonld = False
        self._in_title = False
        self._noise_depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.stack.append(tag)
        if tag in self.NOISE:
            self._noise_depth += 1
        if tag == "script" and a.get("type", "").strip().lower() == "application/ld+json":
            self._in_jsonld = True
            self.jsonld_raw.append("")
        if tag == "title":
            self._in_title = True
        if tag in ("h1", "h2", "h3", "h4"):
            self._current_heading = [tag, ""]
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key and a.get("content"):
                self.metas[key.lower()] = a["content"]
        if tag == "a":
            href = (a.get("href") or "").lower()
            if href.startswith("tel:"):
                self.tel_links += 1
            elif href.startswith("mailto:"):
                self.mailto_links += 1
        if tag == "time" and a.get("datetime"):
            self.time_tags.append(a["datetime"])

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack.pop() != tag:
                pass
        if tag in self.NOISE and self._noise_depth:
            self._noise_depth -= 1
        if tag == "script":
            self._in_jsonld = False
        if tag == "title":
            self._in_title = False
        if tag in ("h1", "h2", "h3", "h4") and self._current_heading:
            self.headings.append((self._current_heading[0], " ".join(self._current_heading[1].split())))
            self._current_heading = None

    def handle_data(self, data):
        if self._in_jsonld:
            self.jsonld_raw[-1] += data
            return
        if self._in_title:
            self.title += data
        if any(t in self.SKIP for t in self.stack):
            return
        if self._current_heading is not None:
            self._current_heading[1] += data
        if self._noise_depth == 0:
            self.text_parts.append(data)


def fetch(url, accept_error=False):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept-Language": "es-ES,es;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            body = r.read()
            charset = r.headers.get_content_charset() or "utf-8"
            return r.status, body.decode(charset, errors="replace"), dict(r.headers)
    except urllib.error.HTTPError as e:
        if accept_error:
            return e.code, "", dict(e.headers or {})
        raise
    except urllib.error.URLError as e:
        raise RuntimeError(f"No se pudo conectar con {url}: {e.reason}") from e


def parse_robots(text):
    """Devuelve lista de grupos: {agents:[...], rules:[(allow|disallow, path)]}."""
    groups, current = [], None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        key, val = [s.strip() for s in line.split(":", 1)]
        key = key.lower()
        if key == "user-agent":
            if current and current["rules"]:
                groups.append(current)
                current = None
            if current is None:
                current = {"agents": [], "rules": []}
            current["agents"].append(val.lower())
        elif key in ("allow", "disallow") and current is not None:
            current["rules"].append((key, val))
    if current:
        groups.append(current)
    return groups


def bot_allowed(groups, bot, path="/"):
    """True si el bot puede rastrear `path`. Regla más larga gana."""
    name = bot.lower()
    matching = [g for g in groups if name in g["agents"]]
    if not matching:
        matching = [g for g in groups if "*" in g["agents"]]
    if not matching:
        return True, "sin reglas"
    rules = [r for g in matching for r in g["rules"]]
    best = None
    for kind, p in rules:
        if p == "" and kind == "disallow":
            continue
        if path.startswith(p.rstrip("$")) or p == "/":
            if best is None or len(p) > len(best[1]) or (len(p) == len(best[1]) and kind == "allow"):
                best = (kind, p)
    if best is None:
        return True, "sin regla aplicable"
    return best[0] == "allow", f"{best[0].capitalize()}: {best[1]}"


def detect_cms(html, headers):
    hay = html[:200000] + " " + " ".join(f"{k}: {v}" for k, v in headers.items())
    found, builders = None, []
    for name, patterns in CMS_SIGNATURES:
        if any(re.search(p, hay, re.IGNORECASE) for p in patterns):
            if name == "Elementor":
                builders.append(name)
            elif found is None:
                found = name
    return found, builders


def extract_jsonld(raw_blocks):
    blocks, types, errors = [], [], 0
    for raw in raw_blocks:
        raw = raw.strip()
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            errors += 1
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if isinstance(item, dict) and "@graph" in item:
                items.extend(i for i in item["@graph"] if isinstance(i, dict))
                continue
            if not isinstance(item, dict):
                continue
            t = item.get("@type")
            t = t if isinstance(t, list) else [t]
            types.extend(str(x) for x in t if x)
            blocks.append({
                "type": t,
                "name": item.get("name"),
                "telephone": item.get("telephone"),
                "url": item.get("url"),
                "address": bool(item.get("address")),
                "datePublished": item.get("datePublished"),
                "author": (item.get("author") or {}).get("name") if isinstance(item.get("author"), dict) else item.get("author"),
                "faq_questions": len(item.get("mainEntity", [])) if "FAQPage" in t else None,
            })
    return blocks, sorted(set(types)), errors


def analyze(html, robots_txt, base, headers=None, llms_status=None, page_status=200):
    headers = headers or {}
    p = PageParser()
    p.feed(html)
    visible = " ".join(" ".join(p.text_parts).split())
    blocks, types, errors = extract_jsonld(p.jsonld_raw)

    groups = parse_robots(robots_txt or "")
    bots = {}
    for bot, info in AI_BOTS.items():
        allowed, rule = bot_allowed(groups, bot)
        bots[bot] = {**info, "permitido": allowed, "regla": rule}

    questions = [h for _, h in p.headings if h.strip().endswith("?") or h.strip().startswith("¿")
                 or h.lower().split(" ")[0] in QUESTION_WORDS]
    phones = sorted(set(m.group().strip() for m in PHONE_RE.finditer(visible)))
    emails = sorted(set(EMAIL_RE.findall(html)))
    addresses = sorted(set(m.group().strip() for m in ADDRESS_RE.finditer(visible)))[:5]
    postal = sorted(set(POSTAL_RE.findall(visible)))[:5]
    numbers_with_units = len(re.findall(r"\d[\d.,]*\s?(?:€|%|m²|m2|años|min|h|km|kg|clientes|instalaciones|proyectos)", visible))

    dates = [d for d in [p.metas.get("article:published_time"), p.metas.get("date")] if d]
    dates += p.time_tags[:3]
    dates += [b["datePublished"] for b in blocks if b.get("datePublished")]
    authors = [b["author"] for b in blocks if b.get("author")] + [p.metas.get("author")] if p.metas.get("author") else [b["author"] for b in blocks if b.get("author")]

    cms, builders = detect_cms(html, headers)

    return {
        "url": base,
        "estado_http": page_status,
        "cms": cms,
        "constructores": builders,
        "rastreadores": bots,
        "rastreadores_citacion_bloqueados": [b for b, v in bots.items() if v["citacion"] and not v["permitido"]],
        "robots_txt_existe": bool(robots_txt),
        "llms_txt_status": llms_status,
        "jsonld": {"bloques": len(blocks), "tipos": types, "errores_parseo": errors, "detalle": blocks},
        "contenido": {
            "html_caracteres": len(html),
            "texto_visible_caracteres": len(visible),
            "palabras": len(visible.split()),
            "title": " ".join(p.title.split()),
            "meta_description": p.metas.get("description"),
            "og_site_name": p.metas.get("og:site_name"),
            "h1": [h for t, h in p.headings if t == "h1"],
            "encabezados_total": len(p.headings),
            "encabezados_pregunta": questions,
            "cifras_con_unidad": numbers_with_units,
            "fechas": dates[:5],
            "autores": [a for a in authors if a][:3],
        },
        "entidad": {
            "telefonos": phones[:5],
            "enlaces_tel": p.tel_links,
            "emails": emails[:3],
            "enlaces_mailto": p.mailto_links,
            "direcciones": addresses,
            "codigos_postales": postal,
        },
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", nargs="?", help="URL a analizar")
    ap.add_argument("--html", help="archivo HTML local en lugar de descargar")
    ap.add_argument("--robots", help="archivo robots.txt local")
    ap.add_argument("--base", help="URL base cuando se usan archivos locales")
    args = ap.parse_args()

    if not args.url and not args.html:
        ap.error("indica una URL o --html")

    try:
        if args.html:
            html = open(args.html, encoding="utf-8", errors="replace").read()
            robots = open(args.robots, encoding="utf-8", errors="replace").read() if args.robots else ""
            base = args.base or "local"
            result = analyze(html, robots, base)
        else:
            url = args.url if args.url.startswith("http") else "https://" + args.url
            parsed = urllib.parse.urlparse(url)
            origin = f"{parsed.scheme}://{parsed.netloc}"
            status, html, headers = fetch(url, accept_error=True)
            if status in (401, 403, 429, 503) or (status == 200 and len(html) < 500 and re.search(r"challenge|captcha|cloudflare", html, re.I)):
                print(json.dumps({
                    "error": f"El servidor ha respondido {status} o una página de desafío. "
                             "Puede que un firewall bloquee a los bots aunque robots.txt los permita. "
                             "Pide al usuario el HTML y analízalo con --html.",
                    "url": url, "estado_http": status,
                }, ensure_ascii=False, indent=2))
                sys.exit(2)
            if status >= 400:
                print(json.dumps({"error": f"La URL devuelve {status}.", "url": url}, ensure_ascii=False, indent=2))
                sys.exit(2)
            r_status, robots, _ = fetch(origin + "/robots.txt", accept_error=True)
            robots = robots if r_status == 200 else ""
            l_status, _, _ = fetch(origin + "/llms.txt", accept_error=True)
            result = analyze(html, robots, url, headers, l_status, status)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except RuntimeError as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False, indent=2))
        sys.exit(2)


if __name__ == "__main__":
    main()
