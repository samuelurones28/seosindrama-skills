# Glosario: del término técnico a lo que entiende el cliente

Ordenado por frecuencia con la que aparece en las 731 auditorías de la
muestra. La analogía de la tienda ("abrir la tienda y tardar X segundos en
encender el escaparate") es la más natural y por eso es la que más se repite;
usa las alternativas para no decir lo mismo tres veces en un mismo informe.

| Término técnico | Cómo se dice al cliente | Analogías (elige una) |
|---|---|---|
| LCP (Largest Contentful Paint) | "El contenido principal tarda X s en aparecer" | Tienda: entras y el escaparate tarda X s en encenderse. Restaurante: te sientan y la carta tarda X s en llegar. Coche: giras la llave y el motor tarda X s en arrancar. |
| JavaScript no utilizado | "Se descarga código que la página no usa" | Mudanza: cargar el camión con cajas que nunca se abren. Caja de herramientas completa para colgar un cuadro. Maleta con ropa de todas las estaciones para un fin de semana. |
| JavaScript bloqueante (render-blocking) | "Hay un archivo que obliga a la página a esperar antes de mostrar nada" | Puerta: alguien bloquea la entrada rellenando un formulario antes de dejar pasar a los demás. Cocina: no se sirve ningún plato hasta que se termina el postre. |
| Contraste insuficiente | "Hay textos o botones que se leen mal" | Cartel de "abierto" con letras casi del mismo color que la pared. Menú con letras grises sobre fondo claro. Señal de tráfico descolorida. |
| CSS no utilizado | "Se descargan estilos que esta página no necesita" | Escaparate decorado con carteles de todas las campañas del año. Armario entero de ropa que nadie se pone. Vajilla completa para servir un café. |
| Cadenas de redirecciones | "La visita pasa por varias direcciones antes de llegar a la buena" | Cartel en la puerta que te manda a otra puerta y luego a otra. Llamada que pasa por tres extensiones antes de la correcta. |
| Meta description ausente o genérica | "Google decide qué texto mostrar debajo de tu enlace" | Escaparate sin cartel: la tienda existe pero nadie entiende qué vende. Tarjeta de visita sin especialidad. |
| Title ausente, duplicado o largo | "El nombre con el que Google presenta tu página está mal puesto" | Rótulo de la tienda vacío o con el nombre del vecino. Carpeta sin etiqueta en un archivador. |
| TBT (Total Blocking Time) / TTI | "La página se ve pero tarda X s en responder a los toques" | Tienda con luces encendidas pero nadie atiende durante X s. Camarero que tarda X s en acercarse. Ascensor que se ve pero no responde al botón. |
| INP (Interaction to Next Paint) | "Cuando el visitante toca un botón, la respuesta tarda X ms" | Interruptor que tarda en encender la luz. Timbre que suena un segundo después de pulsarlo. |
| CLS (Cumulative Layout Shift) | "La página se mueve mientras carga y el visitante pierde el sitio" | Leer un cartel mientras alguien lo sacude. Periódico al que te cambian los titulares de sitio. Estantería que se recoloca cuando vas a coger algo. |
| Imágenes en formato antiguo (JPG/PNG en vez de WebP/AVIF) | "Las imágenes pesan más de lo necesario" | Catálogo impreso en papel fotográfico cuando basta papel normal. Enviar la foto original de la cámara por WhatsApp. |
| Imágenes sin dimensionar / sobredimensionadas | "Se envían imágenes enormes para mostrarlas pequeñas" | Póster de dos metros para colgarlo en un marco de 10x15. |
| Caché (cache policy) | "El navegador vuelve a descargar cada vez cosas que no han cambiado" | Comprar el periódico de ayer cada mañana. Pedir el DNI al cliente habitual cada vez que entra. |
| TTFB (Time to First Byte) | "El servidor tarda X s en empezar a responder" | Llamar y que el teléfono suene X s antes de que descuelguen. Restaurante donde tardan en darte mesa aunque esté vacío. |
| robots.txt | "Un archivo que dice a Google (y a la IA) qué puede leer" | Cartel de "personal autorizado" en las puertas del local. Lista de invitados en la entrada. |
| Sitemap | "Un índice de todas las páginas para que Google no se pierda" | Plano del centro comercial junto a la entrada. Índice de un libro. |
| Canonical | "Cuando hay dos versiones de una página, cuál es la oficial" | Dos entradas al mismo local; una es la principal. Original y fotocopia. |
| HTTPS / certificado | "La conexión no está cifrada" o "el certificado está mal" | Tienda sin persiana ni cerradura. Sobre abierto en lugar de cerrado. |
| Alt de imagen | "Las imágenes no tienen descripción para Google ni para personas con lector de pantalla" | Fotos en un álbum sin pie de foto. Producto sin etiqueta en la estantería. |
| Orden de encabezados (h1, h2...) | "Los títulos de la página no están ordenados y cuesta entender su estructura" | Libro con capítulos numerados al azar. Carta de restaurante con los postres entre los entrantes. |
| Enlaces sin texto descriptivo ("pincha aquí") | "Los enlaces no dicen a dónde llevan" | Puertas sin rótulo en un pasillo. Botones de ascensor sin número. |
| Fuentes web (font-display) | "El texto tarda en aparecer porque espera a que llegue la tipografía" | Cartel que se cuelga en blanco hasta que llega el rotulista. |
| Recursos de terceros (YouTube, chat, mapas, analítica) | "Hay elementos externos que frenan tu página aunque no sean tuyos" | Alquilar un rincón del local a otro negocio que bloquea el pasillo. |
| Tareas largas (long tasks) | "La página se queda ocupada haciendo cálculos y no atiende" | Dependiente contando la caja mientras hay cola. |
| Viewport / móvil no adaptado | "La página no se ajusta a la pantalla del móvil" | Cartel de carretera pegado en el escaparate: hay que alejarse para leerlo. |
| Datos de laboratorio (Lighthouse) vs de campo (CrUX) | "Una prueba simulada" vs "lo que han vivido tus visitantes reales" | Prueba de coche en circuito vs consumo real en tu trayecto diario. |

## Reglas de uso

- Una analogía por hallazgo, en `explicacion_sencilla`. No mezcles dos.
- Si en un informe salen tres hallazgos de velocidad, usa tres analogías
  distintas (tienda, restaurante, coche). Nunca tres tiendas.
- La analogía nunca contiene la cifra técnica en formato técnico: "tarda 14
  segundos", no "tiene un LCP de 14 s".
- Si el usuario ha dicho el sector, la analogía se adapta: para un
  restaurante, la de la carta; para un taller, la del coche; para una
  clínica, la de la sala de espera.
