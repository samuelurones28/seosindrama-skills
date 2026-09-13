# localbusiness.json, campo a campo

Plantilla genérica. Datos ficticios. Se copia y se recortan los campos que
el negocio no tenga; nunca se rellenan con datos inventados.

| Campo | Obligatorio | Qué es y cómo rellenarlo |
|---|---|---|
| `@context` | Sí | Siempre `https://schema.org` |
| `@type` | Sí | El subtipo del sector (ver `references/tipos-schema.md`). `LocalBusiness` solo si nada encaja |
| `@id` | Recomendado | URL de la web + `#negocio`. Fijo, igual en todas las páginas. Permite que otros bloques (`WebPage`, `Article`) apunten a él con `"publisher": {"@id": "..."}` |
| `name` | Sí | Nombre exacto de Google Business Profile |
| `alternateName` | No | Razón social u otra forma en que se conoce al negocio. Útil para que la IA una "Ferretería Ejemplo" con "Ferretería Ejemplo S.L." |
| `description` | Recomendado | Dos frases con qué hace, dónde y qué lo distingue. Sin superlativos |
| `url` | Sí | Portada, con `https://` y sin barra final si la web no la usa |
| `telephone` | Sí | Formato `+34 XXX XXX XXX`. Uno solo; si hay varios, el principal |
| `email` | No | Solo si el negocio lo publica en la web |
| `image` | Recomendado | URL absoluta de una foto del local o del equipo. Google la puede mostrar |
| `logo` | No | URL absoluta del logo (mínimo 112x112 px) |
| `priceRange` | Recomendado | `€` a `€€€€`. Google lo muestra en la ficha |
| `foundingDate` | No | Año (`"1994"`) o fecha ISO |
| `currenciesAccepted` | No | `EUR` |
| `paymentAccepted` | No | Texto libre: "Efectivo, Tarjeta, Bizum" |
| `address` | Sí | Objeto `PostalAddress` completo. `addressRegion` es la provincia; `addressCountry` siempre `ES` |
| `geo` | No | Coordenadas decimales. Se sacan de Google Maps (clic derecho sobre el local). Ayuda cuando la dirección es ambigua |
| `hasMap` | No | URL de la ficha en Google Maps |
| `areaServed` | Según caso | Para negocios que reciben público, la ciudad. Para negocios que se desplazan, lista de localidades o un `GeoCircle` |
| `openingHoursSpecification` | Recomendado | Un objeto por tramo horario. Los días en inglés (`Monday`...). Horario partido = dos objetos. Días cerrados no se listan. Para 24 h: `opens: "00:00"`, `closes: "23:59"` |
| `sameAs` | Recomendado | Solo perfiles reales que el usuario haya dado: Google Maps, Instagram, Facebook, LinkedIn, directorios sectoriales. Refuerza la entidad |
| `aggregateRating` | Solo si las reseñas están en la web | `ratingValue`, `reviewCount` (o `ratingCount`), `bestRating`. Nunca copiar las cifras de Google Maps: Google lo considera reseñas autoservidas y puede ignorar todo el bloque |

## Cómo incrustarlo

```html
<script type="application/ld+json">
{ ...contenido del JSON... }
</script>
```

Antes de pegarlo, sustituir cualquier `</` que aparezca dentro de un valor
de texto por `<\/`. En JavaScript:

```js
const safe = JSON.stringify(data).replace(/<\//g, "<\\/").replace(/<!--/g, "<\\!--");
```
