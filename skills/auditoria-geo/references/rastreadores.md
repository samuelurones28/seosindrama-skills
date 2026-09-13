# Rastreadores de IA: user-agents y qué controla cada uno

**Última revisión: 13 de septiembre de 2026.** Los nombres cambian; antes de
publicar una versión nueva, contrastar con la documentación oficial de cada
proveedor (OpenAI: developers.openai.com/api/docs/bots · Anthropic: centro de
ayuda "Does Anthropic crawl data from the web" · Perplexity: docs.perplexity.ai
sobre crawlers · Google: developers.google.com/search/docs/crawling-indexing ·
Apple: support.apple.com sobre Applebot).

Distinción que importa para GEO: hay bots de **entrenamiento** (recogen texto
para entrenar modelos), bots de **búsqueda/indexación** (alimentan el índice
que usa el motor para responder) y bots de **usuario** (visitan una página
cuando un usuario lo pide en el chat). Bloquear los de entrenamiento es una
decisión legítima y no afecta a las citas. Bloquear los de búsqueda o de
usuario sí quita a la web de las respuestas.

| User-agent | Proveedor | Tipo | Afecta a la citación | Respeta robots.txt |
|---|---|---|---|---|
| `GPTBot` | OpenAI | Entrenamiento | No | Sí |
| `OAI-SearchBot` | OpenAI | Búsqueda (ChatGPT search) | **Sí** | Sí |
| `ChatGPT-User` | OpenAI | Usuario (navegación, GPTs, acciones) | **Sí** | OpenAI ya no garantiza que cumpla robots.txt |
| `ClaudeBot` | Anthropic | Entrenamiento | No | Sí |
| `Claude-SearchBot` | Anthropic | Búsqueda | **Sí** | Sí |
| `Claude-User` | Anthropic | Usuario | **Sí** | Sí |
| `PerplexityBot` | Perplexity | Búsqueda/indexación | **Sí** | Sí |
| `Perplexity-User` | Perplexity | Usuario | **Sí** | Generalmente no |
| `Google-Extended` | Google | Token de control: entrenamiento y grounding de Gemini | Parcial: no afecta a Search ni a AI Overviews (usan Googlebot); sí a Gemini | Sí |
| `Googlebot` | Google | Búsqueda; también alimenta AI Overviews y AI Mode | **Sí** | Sí |
| `Applebot` | Apple | Búsqueda (Siri, Spotlight, Safari) | Sí para Apple | Sí |
| `Applebot-Extended` | Apple | Token de control: entrenamiento | No | Sí |
| `Bingbot` | Microsoft | Búsqueda; alimenta Copilot | **Sí** | Sí |
| `meta-externalagent` | Meta | Entrenamiento | No | Sí |
| `Amazonbot` | Amazon | Alexa y modelos de Amazon | Poco | Sí |
| `DuckAssistBot` | DuckDuckGo | Búsqueda (DuckAssist) | Sí para DDG | Sí |
| `MistralAI-User` | Mistral | Usuario (Le Chat) | Sí para Mistral | Sí |
| `CCBot` | Common Crawl | Entrenamiento (datasets públicos) | No directamente | Sí |
| `Bytespider` | ByteDance | Entrenamiento | No | Cumplimiento irregular documentado |

Nombres obsoletos que aún aparecen en robots.txt antiguos y no hacen nada:
`anthropic-ai`, `Claude-Web`, `ChatGPT-Plugins`, `cohere-ai`.

## Cómo se evalúa el acceso

1. Descargar `/robots.txt`. Si devuelve 404, no hay restricciones: todos
   permitidos.
2. Para cada user-agent de la tabla, buscar el bloque `User-agent:` más
   específico que le aplique (coincidencia exacta e insensible a mayúsculas;
   si no hay, el bloque `*`).
3. Dentro de ese bloque, aplicar las reglas `Allow` / `Disallow` a la ruta
   `/`. `Disallow: /` bloquea; `Disallow:` vacío o ausencia de reglas permite.
4. Un `Disallow: /` en el bloque `*` bloquea a todos los que no tengan bloque
   propio, incluidos los de búsqueda. Es el error más común: webs que
   "bloquean bots" y se quitan de ChatGPT sin querer.

## Qué recomendar

- **Configuración recomendada para una pyme que quiere ser citada:**

```
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /
```

  Y, si el negocio no quiere alimentar entrenamiento (decisión suya, no de
  la skill):

```
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: CCBot
Disallow: /
```

- Nunca recomendar bloquear `Googlebot` ni `Bingbot`: son la puerta de AI
  Overviews y Copilot además de la búsqueda clásica.
- `llms.txt` (`/llms.txt`, Markdown con descripción del sitio y enlaces a lo
  importante) no está adoptado oficialmente por ningún motor grande a fecha
  de revisión. Cuenta como señal menor: fácil de añadir, bajo coste, no
  garantiza nada. No presentarlo como requisito.
- Un firewall/WAF (Cloudflare, etc.) puede bloquear bots con 403 o desafíos
  aunque robots.txt los permita. Si el script recibe 403 o una página de
  desafío, el informe lo dice como hallazgo separado: "el servidor rechaza
  al user-agent aunque robots.txt lo permite".
