# Umbrales y ponderación

## Core Web Vitals

Umbrales oficiales de Google. La etiqueta se calcula sobre el percentil 75
de los usuarios reales (CrUX) cuando existe; si no, sobre la simulación de
Lighthouse, y hay que decirlo en el informe.

| Métrica | Bueno | Necesita mejora | Pobre | Qué mide |
|---|---|---|---|---|
| LCP | ≤ 2.500 ms | 2.500 – 4.000 ms | > 4.000 ms | Cuándo aparece el elemento principal visible |
| CLS | ≤ 0,1 | 0,1 – 0,25 | > 0,25 | Cuánto se mueve la página mientras carga |
| INP | ≤ 200 ms | 200 – 500 ms | > 500 ms | Cuánto tarda en responder a una interacción |
| FID (obsoleta) | ≤ 100 ms | 100 – 300 ms | > 300 ms | Solo aparece en informes antiguos; Google la retiró en 2024 y la sustituyó por INP. Si la entrada trae FID y no INP, tradúcela igual pero indica en la nota técnica que es la métrica antigua |

Métricas de laboratorio que Lighthouse usa además de las anteriores:

| Métrica | Bueno | Necesita mejora | Pobre |
|---|---|---|---|
| FCP | ≤ 1.800 ms | 1.800 – 3.000 ms | > 3.000 ms |
| TBT | ≤ 200 ms | 200 – 600 ms | > 600 ms |
| Speed Index | ≤ 3.400 ms | 3.400 – 5.800 ms | > 5.800 ms |
| TTFB | ≤ 800 ms | 800 – 1.800 ms | > 1.800 ms |

## Puntuación ponderada de seosindrama

Cuando la entrada es una auditoría de seosindrama.com o el usuario pide
"la nota global" a partir de las cuatro categorías de Lighthouse:

| Categoría | Peso |
|---|---|
| Rendimiento | 45 % |
| SEO | 25 % |
| Accesibilidad | 20 % |
| Buenas prácticas | 10 % |

`nota = 0,45·rendimiento + 0,25·seo + 0,20·accesibilidad + 0,10·buenas_practicas`

Rangos del resumen global: menos de 40 · 40–69 · 70–89 · 90 o más. En la
muestra de 731 auditorías: 0 %, 18 %, 66 % y 16 % respectivamente, con media
78,6. Estos porcentajes describen a la pyme que llega a una herramienta de
auditoría, no a "las webs españolas"; no los uses como estadística general.

## Formato de cifras en la salida

- Separador de miles con punto y decimales con coma: 1.312 KiB, 2,5 s.
- Milisegundos por encima de 1.000 se pasan a segundos con una decimal:
  "14,0 s", no "14.030 ms". En la nota técnica pueden ir en ms.
- Se conserva la unidad de la herramienta (KiB si Lighthouse dice KiB).
- Los ahorros estimados van siempre acompañados de "estimación" o
  "potencial".
