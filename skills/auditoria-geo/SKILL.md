---
name: auditoria-geo
description: Audita si una web está preparada para que ChatGPT, Perplexity, Gemini, Claude o Copilot la lean, la entiendan y la citen (GEO, Generative Engine Optimization, también llamado AEO o SEO para IA). Comprueba el acceso de los rastreadores de IA en robots.txt, los datos estructurados JSON-LD, la densidad y estructura del contenido, las señales de entidad (nombre, dirección y teléfono consistentes), el contenido citable y la existencia de llms.txt, y devuelve una puntuación provisional con plan de acción por prioridad y por CMS. Úsala siempre que el usuario pregunte si la IA recomienda su negocio, por qué ChatGPT no le menciona, pida una auditoría GEO o "de IA", quiera salir en ChatGPT o Perplexity, o pregunte por llms.txt, GPTBot, ClaudeBot o PerplexityBot. Also use for AI search visibility audit, GEO audit, get cited by ChatGPT, LLM readiness check, AI crawler access.
---

# Auditoría GEO: ¿puede la IA leer, entender y citar esta web?

Los motores de respuesta (ChatGPT, Perplexity, Gemini, Claude) no posicionan
páginas: eligen fuentes. Para ser elegido hay que ser accesible, legible como
entidad, y tener algo citable. Esta skill lo comprueba sobre una URL.

## Cuándo usarla y cuándo no

**Úsala** cuando el usuario quiera saber si su web (o la de un cliente) está
preparada para los motores de IA, o cuando pregunte por rastreadores,
llms.txt o por qué la IA no le recomienda.

**No la uses** para:

- Medir posiciones en Google, tráfico ni palabras clave. Eso es SEO clásico.
- Medir velocidad o Core Web Vitals. Para eso está PageSpeed y, para
  explicarlo al cliente, `traducir-a-cliente`.
- Generar el JSON-LD. Si falta schema, esta skill lo detecta y recomienda;
  `schema-negocio-local` lo genera.

## Flujo

1. **Obtener los datos.**
   - Si hay entorno de ejecución: `python3 scripts/geo_check.py https://ejemplo.es`
     devuelve un JSON con todo lo que la skill necesita. Sin dependencias
     externas. Si la web no responde o bloquea el user-agent, el script lo
     dice claramente; no interpretes un fallo de red como "la web bloquea a la
     IA".
   - Si no hay entorno: pide al usuario el HTML de la portada y el contenido
     de `/robots.txt`, o léelos con las herramientas de navegación que tengas.
     El script acepta también `--html archivo.html --robots robots.txt` para
     analizar archivos locales.
2. **Aplicar los criterios** de `references/senales-ia.md`, dimensión por
   dimensión, anotando la evidencia literal (qué línea del robots.txt, qué
   `@type`, cuántos caracteres).
3. **Puntuar y redactar** el informe con el formato de abajo.
4. Si el usuario puede lanzar una consulta a un motor de IA, proponerle la
   pregunta tipo cliente (ver dimensión 5) y clasificar la respuesta.

## Las cinco dimensiones y su peso

Pesos **provisionales** hasta que se cierre el informe premium de
seosindrama.com; están marcados así en el informe.

| # | Dimensión | Peso | Qué comprueba |
|---|---|---|---|
| 1 | Acceso de rastreadores de IA | 25 | robots.txt no bloquea a los bots de búsqueda/citación (OAI-SearchBot, Claude-SearchBot, PerplexityBot, etc.). Bloquear los de entrenamiento (GPTBot, ClaudeBot, CCBot) no penaliza. llms.txt suma poco pero suma. Detalle en `references/rastreadores.md` |
| 2 | Datos estructurados | 20 | Hay JSON-LD válido; el `@type` corresponde al negocio; tiene `name`, `address`, `telephone`, `url`; hay `FAQPage` si la página responde preguntas |
| 3 | Contenido citable | 25 | Texto visible suficiente (umbral: 5.000 caracteres de HTML como mínimo, mejor medir texto visible), estructura de encabezados, preguntas en encabezados con respuesta directa debajo (*answer first*), datos propios que un motor pueda citar (*information gain*): cifras, precios, comparativas, casos |
| 4 | Entidad consistente | 20 | Nombre, dirección y teléfono (NAP) aparecen en el HTML, coinciden con el JSON-LD y con lo que el usuario dice tener en Google Business Profile. Autor y fecha en contenidos editoriales |
| 5 | Visibilidad actual | 10 | Solo si el usuario lanza la pregunta tipo cliente a un motor y pega la respuesta. La skill **no** llama a APIs. Si no hay dato, esta dimensión se marca "no medida" y la puntuación se calcula sobre 90 |

**Puntuación:** cada dimensión se valora 0–100 con los criterios de
`senales-ia.md` y se pondera. Se presenta como "X / 100 (provisional)".

### Dimensión 5: la pregunta tipo cliente

Se construye así: `recomiéndame las mejores opciones de <servicio> en
<localidad>`. Ejemplo: "recomiéndame las mejores opciones de fisioterapia en
Valladolid". Variantes de marca a comprobar en la respuesta: nombre exacto,
nombre sin forma jurídica (S.L., S.A.), nombre sin tildes, dominio. La
clasificación:

- **Aparece**: el nombre o el dominio están en la respuesta como
  recomendación.
- **Mención parcial**: aparece una variante, o aparece pero no como
  recomendación (por ejemplo, en una lista larga sin comentario).
- **No aparece**.

## Formato del informe

```markdown
# Auditoría GEO de ejemplo.es
Fecha · URL analizada · CMS detectado (si hay firma) · Puntuación: 62 / 100 (provisional)

## Resumen
Tres frases: qué está bien, qué es lo más urgente, qué tipo de negocio parece
ser según las señales encontradas.

## Resultado por dimensión
| Dimensión | Estado | Evidencia |
|---|---|---|
| Acceso de rastreadores | ✅ Correcto | robots.txt sin reglas para bots de IA; llms.txt no existe (404) |
| Datos estructurados | ⚠️ Parcial | JSON-LD con @type WebSite; falta LocalBusiness |
| Contenido citable | ❌ Insuficiente | 1.870 caracteres de texto visible; 0 preguntas en encabezados |
| Entidad consistente | ⚠️ Parcial | Teléfono detectado (+34 983 ...); dirección no encontrada |
| Visibilidad actual | – No medida | |

## Plan de acción
Ordenado por prioridad. Cada acción: qué hacer, dificultad (fácil / media /
necesita desarrollador), pasos, y cómo validar.

### 1. Añadir JSON-LD LocalBusiness — dificultad: fácil
...

## Cómo validar cuando esté hecho
Volver a ejecutar el script; probar la pregunta tipo cliente en dos motores.
```

La evidencia siempre es literal: qué se encontró en el HTML o en robots.txt,
no una interpretación. "No hay JSON-LD" es evidencia; "la web no está
optimizada" no lo es.

El tono es el de `traducir-a-cliente`: directo, sin alarmismo, sin cifras
inventadas. Si el usuario quiere la versión para enviar al cliente, remite a
esa skill con el informe como entrada.

## Recomendaciones por CMS

Los CMS más frecuentes en la muestra de seosindrama y cómo hacer los dos
cambios que más se repiten en el plan de acción:

| CMS | Añadir JSON-LD | Editar robots.txt |
|---|---|---|
| WordPress | Plugin (Yoast, Rank Math, Schema Pro) o pegar el `<script>` en el `<head>` con un plugin de cabecera/pie o en el tema hijo | Ajustes → Lectura no basta; usar Yoast/Rank Math → Herramientas → Editor de archivos, o subir el archivo por FTP a la raíz |
| Shopify | Editar `theme.liquid` (Tienda online → Temas → Editar código) y pegar el script antes de `</head>` | No se puede editar el archivo directamente; crear plantilla `robots.txt.liquid` desde el editor de temas |
| Wix | Ajustes del sitio → SEO → Datos estructurados (por página) o "Código personalizado" en el `<head>` | Panel → SEO → Robots.txt Editor (solo en planes con dominio propio) |
| Squarespace | Ajustes → Avanzado → Inyección de código → Cabecera | No editable. Squarespace genera el suyo; solo se pueden ocultar páginas concretas |
| IONOS MyWebsite | Sección "HTML personalizado" en la cabecera del sitio | No editable en el creador; sí si es hosting con WordPress |
| Jimdo | Solo en planes Pro/Business: Ajustes → Editar `<head>` | No editable |

Si el CMS no permite editar robots.txt, el plan de acción lo dice y pasa a
la siguiente palanca en lugar de insistir.

## Qué NO hace

- No llama a ChatGPT, Perplexity ni a ninguna API. La visibilidad actual la
  aporta el usuario.
- No mide posiciones en Google ni velocidad.
- No genera el JSON-LD ni el contenido: detecta qué falta y lo prioriza.
- No promete que la IA vaya a citar la web. Describe qué la hace más o menos
  elegible.
- No se dispara con "hazme una auditoría SEO" a secas; solo cuando el
  usuario pregunta por IA, GEO, rastreadores o llms.txt.
