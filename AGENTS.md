# AGENTS.md

Este repo contiene skills SEO/GEO en formato [Agent Skills](https://agentskills.io):
carpetas con un `SKILL.md` que un agente (Claude Code, Codex, Cursor u otro)
carga cuando la tarea del usuario encaja con su `description`.

## Qué hay en `skills/`

| Skill | Qué hace |
|---|---|
| `traducir-a-cliente` | Convierte hallazgos técnicos (PageSpeed, Lighthouse, Screaming Frog, informes de agencia) en explicaciones para un cliente sin perfil técnico |
| `auditoria-geo` | Audita si una web está preparada para que ChatGPT, Perplexity, Gemini o Claude la lean y la citen |
| `schema-negocio-local` | Genera el JSON-LD de schema.org para un negocio local español y explica dónde pegarlo |

## Cómo cargar una skill

1. Lee `skills/<nombre>/SKILL.md` completo. Es corto a propósito (menos de 500 líneas).
2. Carga los archivos de `references/` solo cuando el `SKILL.md` te remita a ellos.
   Son material de consulta, no instrucciones que haya que leer de entrada.
3. Los `templates/` son puntos de partida para copiar y adaptar, no salida final.

## Qué NO hacen las skills

- No ejecutan nada que no esté en `scripts/`. El único script del repo es
  `skills/auditoria-geo/scripts/geo_check.py`, sin dependencias fuera de la
  librería estándar de Python. Si no hay entorno para ejecutarlo, la skill
  funciona igual leyendo el HTML que aporte el usuario.
- No llaman a APIs externas ni a motores de IA. La dimensión de "visibilidad
  actual" de `auditoria-geo` solo se rellena si el usuario lanza la consulta
  por su cuenta y pega el resultado.
- No inventan datos. Si una cifra no está en la entrada, no aparece en la salida.

## Idioma

El cuerpo de las skills está en español. Las `description` llevan palabras
clave en español e inglés para que disparen en ambos idiomas.
