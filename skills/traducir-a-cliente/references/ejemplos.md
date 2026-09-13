# Ejemplos reales, uno por tipo de hallazgo

Ocho hallazgos generados en auditorías reales de seosindrama.com, anonimizados
(dominio sustituido por `ejemplo.es`, sin emails ni nombres de negocio). Cada
uno lleva una nota de por qué funciona. Al final hay una sección con los
errores más habituales de versiones antiguas del mismo prompt, para que no se
repitan.

---

## 1. Velocidad de carga (LCP) — el más frecuente: 75 % de las webs

**El contenido principal tarda 21,4 segundos en aparecer**
Prioridad: alta
Qué supone para el negocio: Los visitantes pueden esperar demasiado antes de
ver el contenido principal y abandonar la página o percibirla como lenta. Esta
medición procede de una simulación de Lighthouse y no demuestra el
comportamiento de todos los visitantes.
Explicado de forma sencilla: Es como entrar en una tienda y tener que esperar
más de veinte segundos para ver el escaparate. Aunque la tienda termine
abriendo, la primera impresión ya se ha retrasado demasiado.
Cómo resolverlo:
1. Confirma qué elemento identifica Lighthouse como el contenido principal y
   qué recursos necesita antes de mostrarse.
2. Prioriza la carga de ese elemento y retrasa recursos no esenciales,
   especialmente el reproductor de YouTube asociado a https://www.youtube.com/...
3. Vuelve a ejecutar Lighthouse en las mismas condiciones y comprueba si el
   tiempo de aparición del contenido principal disminuye.
Nota técnica: Revisa el elemento marcado como LCP en el informe y su cadena
de dependencias; considera cargar el reproductor de YouTube bajo demanda o
después del contenido principal. No confundas LCP con el tiempo de carga
completa de la página.

**Por qué funciona:** el título lleva la cifra y ningún acrónimo. El impacto
va en condicional ("pueden") y aclara que es laboratorio. Los tres pasos
siguen confirmar → resolver → verificar y el segundo cita el recurso
concreto que sí estaba en la entrada (el reproductor de YouTube). La nota
técnica evita un error habitual del desarrollador (confundir LCP con carga
completa).

---

## 2. JavaScript no utilizado — 44 %

**Hay 3.281 KB de código descargado que no se aprovecha**
Prioridad: alta
Qué supone para el negocio: Descargar código innecesario puede retrasar la
aparición del contenido y mantener ocupado el dispositivo durante más tiempo,
especialmente con conexiones o equipos limitados. El ahorro de 6.020 ms es una
estimación de Lighthouse, no una mejora garantizada ni una pérdida medida de
visitantes.
Explicado de forma sencilla: Es como transportar una caja enorme para
entregar solo unos pocos documentos: el viaje tarda más y se consume más
esfuerzo del necesario.
Cómo resolverlo:
1. Confirma si las tres referencias a https://www.youtube.com/... corresponden al
   reproductor de YouTube y si todas se necesitan al abrir la página.
2. Carga el reproductor solo cuando el visitante lo solicite o cuando sea
   necesario, y divide o retrasa el código que no participa en la primera
   pantalla.
3. Repite la auditoría y verifica que disminuyen los 3.281 KB de código no
   utilizado y el tiempo estimado de 6.020 ms.
Nota técnica: Analiza el bundle y las dependencias con Chrome DevTools
Coverage o Lighthouse; aplica carga diferida, división de código y
eliminación de importaciones no usadas cuando proceda. Evita modificar o
duplicar directamente el recurso servido por YouTube: controla su inclusión
desde la integración de la página.

**Por qué funciona:** las dos cifras de la entrada (3.281 KB y 6.020 ms)
aparecen tal cual y el tercer paso las usa como criterio de verificación. La
nota técnica advierte de no tocar un recurso de terceros.

---

## 3. Contraste insuficiente (accesibilidad) — 34 %

**Hay textos con contraste insuficiente: 3 bloques no se leen bien**
Prioridad: media
Qué supone para el negocio: Cuando un visitante no lee bien precios, horarios
o llamadas a la acción, baja la probabilidad de que entre, llame o reserve. En
una web local, eso recorta oportunidades justo en la parte más valiosa de la
visita.
Explicado de forma sencilla: Es como poner el menú con letras grises sobre
fondo claro: la gente se acerca, entrecierra los ojos y se va. No es un fallo
estético, es un cartel difícil de leer.
Cómo resolverlo:
1. Cambia el color del texto en `main.flex-1 > section.py-24 > div.max-w-4xl
   > p.mt-6` para que contraste mejor con el fondo.
2. Ajusta también `div.max-w-5xl > div.grid > div > p.text-sm` y
   `div.grid > div > p.leading-relaxed > a` para que cumplan contraste
   suficiente.
3. Verifica con la herramienta de contraste de Lighthouse o WebAIM que esos
   textos superan el mínimo recomendado.
Nota técnica: Corrige los pares de color afectados hasta cumplir WCAG AA.
Revisa variables de color globales y estados de enlace para no romper
consistencia visual.

**Por qué funciona:** los selectores CSS de la entrada van en los pasos para
que el desarrollador sepa exactamente dónde mirar, pero el cliente no
necesita entenderlos: el título y la analogía ya le dicen qué pasa. Pequeño
matiz: aquí el paso 1 empieza por "cambia" en vez de "confirma"; es
aceptable cuando la entrada ya identifica el elemento exacto y no hay nada
que confirmar.

---

## 4. CSS no utilizado — 32 %

**Tienes 289 KiB de estilos sobrantes que frenan la carga visual**
Prioridad: media
Qué supone para el negocio: Ese exceso de estilos suma 1,35 s de ahorro
potencial y retrasa la percepción de velocidad, justo cuando el usuario decide
si se queda. El ahorro es una estimación de Lighthouse.
Explicado de forma sencilla: Es como vestir el escaparate con carteles de
todas las campañas del año aunque solo vendas una hoy. El cliente tarda más en
entender qué ofreces y se impacienta.
Cómo resolverlo:
1. Recorta `wpo-minify-header-hfe-widgets-style1787754255.min.css` para
   dejar solo los estilos que usa la primera pantalla.
2. Elimina o difiere `accessibility-onetap-front-end.min.css` y
   `wpo-minify-header-hfe-social-share-icons-fontawesome1788379445` si no
   son necesarios al inicio.
3. Vuelve a pasar la prueba y confirma que el peso de estilos baja y la
   página se pinta antes.
Nota técnica: Haz purge de CSS no usado y separa critical CSS del resto.
Revisa estilos generados por Elementor y plugins de terceros para cargarlos
solo donde aportan valor.

**Por qué funciona:** los nombres de archivo delatan WordPress + Elementor y
la nota técnica lo aprovecha sin que el cliente tenga que saberlo. Esa es la
única forma legítima de "presuponer" el CMS: cuando la entrada lo evidencia.

---

## 5. Cadenas de redirecciones — 19 %

**La visita pasa por redirecciones y añade 780 ms potenciales**
Prioridad: media
Qué supone para el negocio: Las redirecciones pueden retrasar la llegada del
contenido, especialmente para visitantes con conexiones lentas. El ahorro
indicado es una estimación y no permite calcular pérdidas de visitas o
conversiones.
Explicado de forma sencilla: Es como llegar a una tienda y encontrar un
cartel que te manda primero a otra dirección antes de abrirte la puerta.
Cómo resolverlo:
1. Confirma con las herramientas de red del navegador qué redirecciones se
   producen al visitar https://ejemplo.es/... y si https://otro-dominio.es/...
   forma parte del recorrido esperado.
2. Reduce la cadena para que la URL inicial lleve directamente a la página
   final, siempre que el comportamiento observado sea intencionado y
   controlable.
3. Vuelve a ejecutar PageSpeed Insights y comprueba si desaparece el aviso y
   si disminuye el ahorro estimado de 780 ms.
Nota técnica: Revisa la cadena HTTP y las cabeceras Location con Chrome
DevTools o curl -I; evita redirecciones encadenadas y apunta la URL inicial
directamente al destino canónico cuando proceda. La auditoría no demuestra
por sí sola la causa ni permite modificar el comportamiento de la URL
externa.

**Por qué funciona:** no da por hecho que la redirección sea un error (puede
ser intencionada) y lo dice en el paso 2. La explicación sencilla es de una
frase; aceptable cuando la analogía se entiende sola.

---

## 6. Meta description ausente — 11 %

**La página no tiene meta descripción: pierdes control sobre el mensaje en
Google**
Prioridad: media
Qué supone para el negocio: Sin meta descripción, Google decide qué texto
mostrar y eso reduce el control sobre el clic. Un texto peor escrito puede
hacer que el visitante elija a un competidor con un mensaje más claro.
Explicado de forma sencilla: Es como poner un escaparate sin cartel: la
tienda existe, pero nadie entiende rápido qué vendes. El cliente mira y sigue
andando porque no le has dado un motivo claro para entrar.
Cómo resolverlo:
1. Escribe una meta descripción única para la página principal con propuesta
   de valor y llamada a la acción.
2. Incluye el servicio principal y el beneficio más fuerte en menos de una
   frase clara.
3. Comprueba en el código fuente y en Search Console que la descripción
   aparece correctamente.
Nota técnica: Añade una etiqueta `<meta name="description" content="...">` en
el `<head>` con un texto único y orientado a clic. Mantén el mensaje alineado
con la intención de búsqueda principal de la home.

**Por qué funciona:** es un hallazgo sin cifra, y el título no se la inventa.
El impacto habla de "control" y "clic", no de CTR ni de porcentajes.

---

## 7. Tiempo hasta interactivo (TTI / TBT)

**La página tarda 9,2 segundos en estar lista para interactuar**
Prioridad: media
Qué supone para el negocio: Los visitantes pueden percibir que la página
responde tarde aunque parte del contenido ya sea visible. Esta medición es de
laboratorio y no representa necesariamente la experiencia de todos los
visitantes.
Explicado de forma sencilla: Es como entrar en una tienda con las luces
encendidas, pero tener que esperar 9,2 segundos hasta que el personal pueda
atenderte.
Cómo resolverlo:
1. Confirma en Chrome DevTools, usando el panel Performance, qué tareas
   mantienen ocupada la página durante esos 9,2 segundos.
2. Prioriza las tareas largas y retrasa o divide el código que no sea
   necesario para la primera interacción, sin asumir todavía qué recurso
   concreto las provoca.
3. Repite la prueba en PageSpeed Insights y comprueba si baja el tiempo de
   interacción sin empeorar las métricas de experiencia ya aprobadas.
Nota técnica: Analiza Long Tasks en Chrome DevTools y el informe de
Lighthouse; aplica code splitting, carga diferida y reducción de trabajo en
el hilo principal solo después de identificar los scripts responsables. No se
han proporcionado recursos concretos, por lo que la causa debe verificarse
antes de cambiar código.

**Por qué funciona:** la entrada no traía recursos concretos y el hallazgo lo
dice en vez de inventarlos ("sin asumir todavía qué recurso concreto las
provoca"). El paso 3 añade una salvaguarda: no empeorar lo que ya aprueba.

---

## 8. Saltos de diseño (CLS) — 8 %

**La página se mueve demasiado: CLS de 0,43**
Prioridad: alta
Qué supone para el negocio: Un desplazamiento de 0,43 es muy alto y puede
hacer que el usuario pierda el sitio justo cuando intenta leer o hacer clic.
En una web de captación, eso puede traducirse en clics erróneos y formularios
abandonados.
Explicado de forma sencilla: Es como intentar leer un cartel mientras alguien
lo está sacudiendo. Cuando todo salta, la gente se cansa y deja de
interactuar.
Cómo resolverlo:
1. Reserva espacio fijo para los bloques que cargan tarde y evita que empujen
   el contenido ya visible.
2. Ajusta los elementos que cambian de tamaño o posición al cargar para que
   no desplacen el resto de la página.
3. Comprueba en móvil que el CLS baja por debajo de 0,1 y que los clics ya no
   se mueven.
Nota técnica: Define dimensiones explícitas en elementos dinámicos y evita
inserciones tardías sin contenedor reservado. Revisa fuentes, banners y
widgets que alteren el layout y valida CLS en CrUX y Lighthouse.

**Por qué funciona:** el título mantiene "CLS" porque el valor 0,43 no tiene
sentido sin el nombre de la métrica; es la excepción razonable a "sin
siglas". El impacto original de la BBDD afirmaba "se traduce en formularios
fallidos"; aquí se ha pasado a condicional, que es lo que exige la regla 4.

---

## Qué NO copiar (errores de versiones antiguas del prompt)

La BBDD también contiene hallazgos de una versión anterior del prompt que
incumplen las restricciones actuales. Reconócelos para no reproducirlos:

| Error | Ejemplo real de la BBDD | Regla que incumple |
|---|---|---|
| Estadística externa no medida | "Google también indica que el 53 % de los usuarios abandona si una web tarda más de 3 s" | Restricción 4: no citar estudios externos |
| Conversión a dinero o conversiones | "cada 100 ms extra de carga puede reducir conversiones alrededor de un 1 %" | Restricción 4 |
| Consecuencia como hecho | "se están perdiendo contactos antes de que vean la propuesta" | Personalidad: consecuencia en condicional |
| Prefijo "Paso 1:" en los pasos | "Paso 1: Elimina o retrasa..." | Formato: cada paso empieza por verbo |
| Sector asumido sin que el usuario lo diga | "Para un restaurante, eso significa..." (cuando la entrada no lo indicaba) | Restricción 5 |
| Prometer resultado en la verificación | "confirma que el CTR mejora" | Restricción 8: verificar la cifra medida, no un resultado de negocio |
| Nombrar el CMS sin evidencia | "Revisa configuración del servidor, CDN y Next.js" cuando nada en la entrada lo indica | Restricción 5 |
| Mezclar dos hallazgos en uno | Un hallazgo de CSS no usado cuyo impacto habla del LCP de 5,9 s | Un hallazgo, una métrica |
