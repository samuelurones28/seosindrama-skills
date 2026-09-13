# Señales que evalúa la auditoría GEO

Por cada dimensión: qué se comprueba, cómo se detecta, umbral de aprobado y
qué recomendar si falla. Los umbrales numéricos de las dimensiones 2, 3 y 4
proceden de los chequeos del `geo-score` de seosindrama.com; los de la
dimensión 1 de `rastreadores.md`. Los pesos son provisionales.

Escala por dimensión: **Correcto** (100), **Parcial** (50), **Insuficiente**
(0), con matices indicados en cada tabla. La puntuación final es la suma
ponderada; si la dimensión 5 no se mide, se divide entre 90 y se reescala.

---

## 1. Acceso de rastreadores de IA (peso 25)

| Comprobación | Cómo se detecta | Aprobado |
|---|---|---|
| robots.txt accesible | GET `/robots.txt`; 404 = sin restricciones | 200 o 404 |
| Bots de búsqueda/usuario permitidos | Parsear bloques por user-agent (ver `rastreadores.md`) | Ninguno de `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Googlebot`, `Bingbot` bloqueado en `/` |
| El servidor no rechaza al bot | El script hace la petición con un user-agent de navegador; si recibe 403/429 o HTML de desafío, lo indica | 200 |
| llms.txt | GET `/llms.txt` | Existe (señal menor) |

**Estados:**
- Correcto: todos los bots de búsqueda/usuario permitidos.
- Parcial: uno o dos bloqueados, o bloqueo solo por `*` sin bloque propio.
- Insuficiente: `Disallow: /` para `*` sin excepciones, o el servidor devuelve
  403 al bot.
- llms.txt suma +5 sobre el estado (máximo 100).

**Si falla:** dar el bloque de robots.txt corregido (de `rastreadores.md`)
y las instrucciones del CMS. Si el bloqueo es del WAF, indicar que hay que
crear una regla de excepción por user-agent verificando la IP contra las
listas publicadas por cada proveedor.

---

## 2. Datos estructurados (peso 20)

| Comprobación | Cómo se detecta | Aprobado |
|---|---|---|
| Hay JSON-LD | `<script type="application/ld+json">` con JSON parseable | Al menos un bloque válido |
| `@type` de negocio | `@type` es `LocalBusiness`, `Organization` o uno de sus subtipos (`Restaurant`, `Dentist`, `LegalService`...); acepta `@graph` | Presente |
| Propiedades mínimas | `name`, `url`, `telephone`, `address` (con `streetAddress`, `addressLocality`, `postalCode`) | Las cuatro |
| `FAQPage` | Bloque con `mainEntity` de tipo `Question` | Presente si la página tiene sección de preguntas |
| Coherencia | `name`/`telephone` del JSON-LD coinciden con el texto visible | Coinciden |

**Estados:**
- Correcto: `@type` de negocio + propiedades mínimas + coherencia.
- Parcial: hay JSON-LD pero solo `WebSite`/`WebPage`/`BreadcrumbList`
  (típico de plugins SEO por defecto), o falta alguna propiedad mínima.
- Insuficiente: sin JSON-LD, o JSON inválido.

**Si falla:** remitir a la skill `schema-negocio-local` con los datos NAP
detectados en el HTML como punto de partida. Si la página responde
preguntas sin `FAQPage`, recomendarlo como bloque adicional.

---

## 3. Contenido citable (peso 25)

| Comprobación | Cómo se detecta | Aprobado |
|---|---|---|
| Densidad textual | Longitud del HTML (umbral heredado del geo-score: ≥ 5.000 caracteres) y, mejor, texto visible tras quitar `script`, `style`, `nav`, `footer` | HTML ≥ 5.000 caracteres **y** texto visible ≥ 1.500 caracteres |
| Estructura | Un `h1`; `h2` que segmentan el contenido | 1 `h1`, ≥ 3 `h2`/`h3` |
| Answer first | Encabezados formulados como pregunta (`¿...?`, o que empiezan por qué/cómo/cuánto/cuándo/dónde/por qué) seguidos de un párrafo que responde en las dos primeras frases | ≥ 2 encabezados-pregunta con respuesta directa |
| Information gain | Datos propios en el texto: cifras con unidad (€, %, m², años, minutos), precios, plazos, comparativas, casos con nombre, listas concretas de servicios | ≥ 3 datos propios en la portada |
| Fechas y autor (editorial) | `article:published_time`, `datePublished`, `<time>`, byline | Presentes en blogs/artículos; no exigible en portadas de negocio |

**Estados:**
- Correcto: densidad + estructura + al menos una de (answer first, info gain).
- Parcial: densidad sí, pero sin preguntas ni datos propios (texto genérico
  tipo "somos una empresa comprometida con la calidad").
- Insuficiente: por debajo del umbral de densidad, o portada que es solo
  imagen/vídeo con dos frases.

**Si falla:**
- Densidad: añadir una sección "Qué hacemos y para quién" con servicios
  concretos, zona, precios orientativos o plazos. Dificultad fácil (lo
  escribe el negocio).
- Answer first: convertir las tres dudas más frecuentes de los clientes en
  `h2` con forma de pregunta y responder en dos frases justo debajo; después
  marcarlas como `FAQPage`. Dificultad fácil.
- Info gain: sustituir adjetivos por datos: "más de 400 instalaciones desde
  2015", "presupuesto en 48 h", "consulta 40 €". Dificultad fácil.

Nota sobre el umbral de 5.000 caracteres de HTML: es una heurística de
producción, no una verdad. Una portada de Wix con 5.000 caracteres de HTML
puede tener 300 de texto. Por eso el script mide las dos cosas y el informe
cita el texto visible.

---

## 4. Entidad consistente (peso 20)

| Comprobación | Cómo se detecta | Aprobado |
|---|---|---|
| Teléfono | Regex de teléfono español: `(\+34|0034)?[ -]?[6789]\d{2}[ -]?\d{3}[ -]?\d{3}` y `tel:` en enlaces | Detectado |
| Email | Regex estándar y `mailto:` | Detectado (informativo) |
| Dirección | Patrones `C/`, `Calle`, `Avda`, `Avenida`, `Plaza`, `Paseo`, `Carretera`, `Polígono` + número; código postal de 5 dígitos; nombre de provincia o localidad | Al menos vía + localidad o CP |
| Nombre de la entidad | `<title>`, `og:site_name`, `name` del JSON-LD, texto del logo | Un solo nombre coherente entre las fuentes |
| Coherencia NAP | Los tres coinciden entre HTML, JSON-LD y lo que el usuario declara en Google Business Profile | Coinciden |
| Autor (editorial) | Byline, `author` en JSON-LD `Article`/`Person` | Presente en artículos |

**Estados:**
- Correcto: teléfono + dirección + nombre coherentes, y coinciden con el
  JSON-LD si existe.
- Parcial: solo teléfono, o dirección sin CP, o nombre distinto entre title y
  JSON-LD (por ejemplo "Clínica Pérez" vs "Clínica Dental Pérez S.L.").
- Insuficiente: ni teléfono ni dirección detectables en el HTML (típico de
  webs que los ponen solo en una imagen o en un formulario).

**Si falla:** poner el NAP en texto plano en el pie de todas las páginas,
exactamente igual que en Google Business Profile, con el teléfono en enlace
`tel:`. Dificultad fácil. Si el nombre varía, elegir uno y unificarlo en web,
GBP, redes y JSON-LD.

---

## 5. Visibilidad actual (peso 10, solo si se mide)

| Comprobación | Cómo | Estado |
|---|---|---|
| Pregunta tipo cliente | El usuario lanza `recomiéndame las mejores opciones de <servicio> en <localidad>` en al menos un motor (ChatGPT con búsqueda, Perplexity, Gemini) y pega la respuesta | Aparece (100) · Mención parcial (50) · No aparece (0) |

Si el usuario prueba en varios motores, media de los estados. Si no mide,
"no medida" y la puntuación se calcula sobre 90.

Advertencia obligatoria en el informe: la respuesta de un motor de IA varía
entre sesiones, ubicaciones y días; una sola consulta es una foto, no una
métrica. Recomendar repetirla mensualmente con la misma pregunta.

---

## Prioridad en el plan de acción

Orden por defecto cuando varias dimensiones fallan:

1. Acceso bloqueado (sin esto, nada más importa).
2. Entidad no detectable (la IA no sabe quién eres).
3. Datos estructurados ausentes.
4. Contenido genérico sin datos ni preguntas.
5. llms.txt y afinado.

Dentro de cada dimensión, primero lo que el negocio puede hacer solo
(dificultad fácil) y después lo que necesita desarrollador.
