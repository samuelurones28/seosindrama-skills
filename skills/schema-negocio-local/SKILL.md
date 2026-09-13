---
name: schema-negocio-local
description: Genera el JSON-LD de datos estructurados schema.org (LocalBusiness y sus subtipos) para un negocio local español a partir de sus datos: nombre, dirección, teléfono, horarios, zona de servicio, redes y valoraciones. Elige el subtipo correcto por sector (restaurante, clínica dental, asesoría, abogado, taller, peluquería, tienda, hotel, inmobiliaria, gimnasio, fontanero, academia, veterinario...), valida los campos obligatorios, escapa el bloque para incrustarlo sin romper el HTML y explica dónde pegarlo según el CMS (WordPress, Shopify, Wix, Squarespace, IONOS, Jimdo). Úsala siempre que el usuario pida schema, datos estructurados, rich snippets, resultados enriquecidos, JSON-LD, "marcar" su negocio para Google o para la IA, o pregunte cómo hacer que Google muestre su horario, teléfono o estrellas. Also use for LocalBusiness schema generator, structured data for local business, JSON-LD for Spanish business, schema.org markup.
---

# Schema para negocio local

Genera un bloque JSON-LD válido, completo hasta donde llegan los datos del
usuario y ni un campo más, y explica dónde pegarlo.

## Cuándo usarla y cuándo no

**Úsala** cuando el negocio tenga dirección física o zona de servicio y el
usuario quiera datos estructurados para Google o para los motores de IA.

**No la uses** para:

- Schema de artículos (`Article`, `BlogPosting`), productos (`Product`),
  eventos, recetas ni vídeos. Si el usuario los pide, dilo y sugiere el tipo
  correcto, pero no lo generes con esta skill.
- Negocios sin presencia local (SaaS, tiendas online sin tienda física).
  Para ellos el tipo es `Organization` y no aplica NAP; puedes generarlo
  como caso simple, avisando de que no tendrá ficha local.
- Si el usuario solo quiere `FAQPage`, genéralo, pero como bloque adicional
  y solo con preguntas que existan de verdad en la página.

## Datos que pedir

Pide lo que falte **en una sola pregunta**, separando obligatorio de
opcional. No generes nada hasta tener los obligatorios; no insistas en los
opcionales.

**Obligatorios**

| Dato | Por qué |
|---|---|
| Nombre exacto del negocio (tal como está en Google Business Profile) | `name` y coherencia NAP |
| Tipo de negocio / sector | elegir `@type` con `references/tipos-schema.md` |
| Dirección completa: vía y número, código postal, localidad, provincia | `address` |
| Teléfono | `telephone`, en formato `+34 ...` |
| URL de la web | `url` y `@id` |

**Opcionales** (si los tiene, mejoran la ficha; si no, se dejan fuera)

Horarios por día con partido de mañana y tarde · rango de precios (`€`,
`€€`, `€€€`) · coordenadas · perfiles reales en redes y directorios (Google
Maps, Instagram, Facebook, LinkedIn, TripAdvisor, Doctoralia) · logo · foto
del local · valoración media y número de reseñas **solo si están publicadas
en la propia web** · zona de servicio (para negocios que se desplazan:
fontaneros, electricistas, cátering) · email · descripción de dos frases ·
año de fundación · métodos de pago · datos específicos del sector (ver
`tipos-schema.md`).

**Nunca pedir ni incluir:** NIF/CIF, datos bancarios, datos personales del
propietario que no sean públicos.

## Reglas de generación

1. **Un solo bloque por página.** Si ya hay JSON-LD del plugin SEO
   (`WebSite`, `WebPage`, `BreadcrumbList`), el bloque de negocio se añade
   como entrada de `@graph` o como script independiente, sin duplicar tipos.
2. **`@id` estable:** `https://ejemplo.es/#negocio` (o `#organization`).
   Sirve para enlazar desde otros bloques y para que Google lo reconozca
   como la misma entidad en todas las páginas.
3. **Teléfono en formato internacional:** `+34 983 123 456`. Sin paréntesis.
4. **`addressCountry: "ES"`** siempre. `addressRegion` con la provincia.
5. **Horarios en `openingHoursSpecification`**, un objeto por tramo. Un
   negocio que abre 9:30–14:00 y 16:30–20:00 lleva dos objetos para esos
   días, no un rango de 9:30 a 20:00. Formato 24 h. Los días cerrados no se
   listan.
6. **`sameAs` solo con perfiles reales** que el usuario haya dado. No
   inventar URLs de Instagram "probables".
7. **`aggregateRating` solo si las reseñas están en la página** y con las
   cifras que el usuario indique. Nunca inventar valoraciones ni copiar las
   de Google Maps (Google lo penaliza como reseñas autoservidas).
8. **Coincidencia exacta NAP** con Google Business Profile: mismo nombre
   (con o sin S.L., pero igual en ambos), misma forma de escribir la
   dirección, mismo teléfono. Si el usuario da variantes, pregunta cuál es la
   de GBP y usa esa.
9. **Escapar `</script>`:** antes de entregar el bloque, sustituir cualquier
   `</` dentro de cadenas por `<\/` para que no rompa el HTML. Lo mismo con
   `<!--`. Es lo que hace la función `safeJsonLd` de seosindrama.
10. **Sin campos vacíos.** Un campo sin dato no aparece; no se rellena con
    `""` ni con "Consultar".
11. **`image` y `logo` con URL absoluta.** Si el usuario da rutas relativas,
    completarlas con la URL de la web.
12. **`priceRange`** con símbolos `€` (uno a cuatro), no con "barato".

## Salida

Tres partes, en este orden:

**1. El bloque listo para pegar**

```html
<script type="application/ld+json">
{ ... }
</script>
```

**2. Qué se ha dejado fuera y por qué**

Lista de campos opcionales no incluidos por falta de datos, con una línea
por campo diciendo qué aportaría ("`geo`: permite a Google situar el local
sin depender de la geocodificación de la dirección"). El usuario decide si
merece la pena volver con esos datos.

**3. Dónde pegarlo**

Según el CMS que haya dicho el usuario. Si no lo ha dicho, pregúntalo o da
la instrucción genérica ("dentro de `<head>`, o al final de `<body>`, en
todas las páginas donde el negocio sea el tema principal; como mínimo la
portada y la página de contacto").

| CMS | Dónde |
|---|---|
| WordPress | Plugin de cabecera (WPCode, "Insert Headers and Footers") → sección Head. Con Rank Math o Yoast, mejor rellenar su módulo de Local SEO y no duplicar |
| Shopify | Tienda online → Temas → Editar código → `theme.liquid`, antes de `</head>` |
| Wix | Ajustes → Avanzado → Código personalizado → Añadir código → Head, "todas las páginas". Wix añade su propio `LocalBusiness` en algunos planes: comprobar con el validador que no haya dos |
| Squarespace | Ajustes → Avanzado → Inyección de código → Cabecera |
| IONOS MyWebsite | Editor → Ajustes → "HTML personalizado" en cabecera |
| Jimdo | Planes Pro/Business: Ajustes → Editar `<head>`. Plan gratuito: no se puede |
| HTML a mano / Next.js / Astro | En el layout, dentro de `<head>`; en React, `dangerouslySetInnerHTML` con el JSON escapado |

## Validación

Después de pegar:

1. **Prueba de resultados enriquecidos de Google** (search.google.com/test/rich-results): confirma que Google lo lee y si hay elegibilidad para resultado enriquecido.
2. **Validador de schema.org** (validator.schema.org): comprueba la sintaxis y los tipos, incluidos los que Google no muestra.

Avisos que se pueden ignorar:

- "Campo recomendado ausente" para `priceRange`, `image`, `geo`,
  `aggregateRating` o `review` cuando el usuario no tiene el dato. Recomendado
  no es obligatorio.
- "No es elegible para resultados enriquecidos" en tipos que Google solo lee
  (`AccountingService`, `LegalService`, `Plumber`...). Sigue siendo útil para
  la entidad y para la IA.

Errores que no se ignoran: `address` sin `streetAddress`, `telephone` en
formato no internacional, `openingHoursSpecification` con `dayOfWeek` mal
escrito (es `Monday`, no `Lunes`), JSON inválido.

## Ejemplo mínimo

Entrada: "Asesoría fiscal Gómez, Calle Santiago 12, 47001 Valladolid,
teléfono 983 12 34 56, web asesoria-gomez-ejemplo.es, abrimos de lunes a viernes de
9 a 14 y de 16 a 19."

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AccountingService",
  "@id": "https://asesoria-gomez-ejemplo.es/#negocio",
  "name": "Asesoría fiscal Gómez",
  "url": "https://asesoria-gomez-ejemplo.es",
  "telephone": "+34 983 123 456",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Santiago 12",
    "postalCode": "47001",
    "addressLocality": "Valladolid",
    "addressRegion": "Valladolid",
    "addressCountry": "ES"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "14:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "16:00",
      "closes": "19:00"
    }
  ]
}
</script>
```

Fuera por falta de datos: `priceRange`, `image`, `logo`, `sameAs`, `geo`,
`email`, `description`. Plantillas completas con todos los campos en
`templates/`.

## Qué NO hace

- No genera schema de artículos, productos, eventos ni recetas.
- No inventa reseñas, valoraciones, horarios, coordenadas ni perfiles
  sociales.
- No audita el schema existente de una web (para eso, `auditoria-geo`).
- No garantiza que Google muestre un resultado enriquecido; eso depende de
  Google.
