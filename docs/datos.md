# De dónde salen los datos

Estas skills no están calibradas con teoría: están calibradas con las auditorías
reales que ha ejecutado [seosindrama.com](https://www.seosindrama.com) sobre webs
de pymes españolas entre marzo y septiembre de 2026.

## La muestra

| Dato | Valor |
|---|---|
| Auditorías completadas | 731 |
| Dominios únicos | 573 |
| Periodo | 18 mar 2026 – 10 sep 2026 |
| Herramienta de medición | Google PageSpeed Insights (Lighthouse + CrUX cuando existe) |

Cada auditoría produce una puntuación ponderada (rendimiento 45 %, SEO 25 %,
accesibilidad 20 %, buenas prácticas 10 %) y hasta tres hallazgos redactados
para un lector no técnico.

## Qué nota sacan

| Rango | Webs | % |
|---|---|---|
| Menos de 40 | 0 | 0 % |
| 40 – 69 | 128 | 18 % |
| 70 – 89 | 484 | 66 % |
| 90 o más | 119 | 16 % |

Nota media: **78,6**. Mediana: **78**. La web típica de una pyme española no está
rota: aprueba con margen, pero arrastra dos o tres problemas concretos.

## Qué falla y en qué proporción

Porcentaje de webs con al menos un hallazgo sobre cada tema:

| Tema | Webs afectadas |
|---|---|
| Velocidad y tiempo de carga (LCP, contenido principal tardío) | 75 % |
| JavaScript no utilizado o bloqueante | 44 % |
| Accesibilidad (contraste, etiquetas, orden de encabezados) | 34 % |
| CSS no utilizado | 32 % |
| Cadenas de redirecciones | 19 % |
| Metadatos (title, meta description) | 11 % |
| Enlaces sin texto descriptivo | 9 % |
| Saltos de diseño al cargar (CLS) | 8 % |
| Imágenes sin optimizar | 5 % |

El **81 %** de las webs tiene al menos un hallazgo de prioridad alta.

## Cómo leer estos números

- **La muestra no es aleatoria.** 550 de las 769 auditorías lanzadas salieron de
  campañas de outreach (webs elegidas a mano) y 217 de tráfico orgánico. Las
  cifras describen la pyme española que llega a una herramienta de auditoría,
  no a toda la web española.
- **La clasificación por tema se hace sobre el título del hallazgo**, no sobre el
  identificador de auditoría de Lighthouse, porque ese campo solo existe en las
  auditorías más recientes. Un hallazgo puede contar en dos temas a la vez.
- **Son mediciones de una URL**, normalmente la portada, no de todo el sitio.
- Aún no hay datos GEO suficientes para publicar (menos de diez informes).
  Se añadirán cuando la muestra sea significativa.

Los datos se recalculan periódicamente desde la base de datos de auditorías.
Última actualización: 13 de septiembre de 2026.
