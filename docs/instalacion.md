# Instalación

Las skills son carpetas con un `SKILL.md`. No hay nada que compilar ni
instalar; basta con que el agente encuentre la carpeta.

## Claude Code

Para un solo proyecto:

```bash
mkdir -p .claude/skills
cp -r seosindrama-skills/skills/traducir-a-cliente .claude/skills/
```

Para todos tus proyectos:

```bash
mkdir -p ~/.claude/skills
cp -r seosindrama-skills/skills/traducir-a-cliente ~/.claude/skills/
```

Claude Code carga la skill cuando la tarea coincide con su `description`.
También puedes invocarla por nombre: `/traducir-a-cliente`.

## Codex, Cursor y otros agentes compatibles con Agent Skills

La ubicación cambia según la herramienta; la más habitual es
`.agents/skills/` en la raíz del proyecto:

```bash
mkdir -p .agents/skills
cp -r seosindrama-skills/skills/auditoria-geo .agents/skills/
```

Consulta la documentación de tu agente para la ruta exacta. Si tu agente no
soporta skills, pégale el contenido de `SKILL.md` como instrucciones del
sistema; las `references/` se le pasan cuando las pida.

## Clon completo

```bash
git clone https://github.com/samuelurones28/seosindrama-skills.git
```

Y enlaza o copia las carpetas de `skills/` que quieras usar. `AGENTS.md`
explica al agente cómo está organizado el repo si lo abre entero.

## Requisitos

- Ninguno para `traducir-a-cliente` y `schema-negocio-local`.
- `auditoria-geo` incluye `scripts/geo_check.py`, que necesita Python 3.8 o
  superior sin dependencias adicionales. Si el agente no puede ejecutar
  Python, la skill funciona igual a partir del HTML que le pegues.

## Actualizar

Las skills cambian cuando cambian los umbrales, los user-agents de los
rastreadores o los datos de la muestra. Vuelve a copiar la carpeta desde el
repo; no hay migración.
