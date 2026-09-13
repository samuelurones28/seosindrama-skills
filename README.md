# seosindrama-skills

Skills de SEO y GEO para agentes de IA (Claude Code, Codex, Cursor y
cualquier herramienta compatible con [Agent Skills](https://agentskills.io)),
calibradas con 731 auditorías reales de webs de pymes españolas.

[English version](README.en.md)

## Qué es esto

Tres skills que enseñan a un agente a hacer bien tres tareas concretas que
en [seosindrama.com](https://www.seosindrama.com) hacemos todos los días:

| Skill | Qué hace | Estado |
|---|---|---|
| [`traducir-a-cliente`](skills/traducir-a-cliente/) | Convierte hallazgos de PageSpeed, Lighthouse, Screaming Frog o un informe de agencia en explicaciones para un cliente sin perfil técnico: título en lenguaje de negocio, impacto, analogía, tres pasos y nota para el desarrollador | Publicada |
| [`auditoria-geo`](skills/auditoria-geo/) | Audita si una web está preparada para que ChatGPT, Perplexity, Gemini o Claude la lean y la citen: rastreadores, JSON-LD, contenido citable, entidad. Incluye script sin dependencias | Provisional |
| [`schema-negocio-local`](skills/schema-negocio-local/) | Genera el JSON-LD `LocalBusiness` correcto para un negocio local español y explica dónde pegarlo según el CMS | Publicada |

## Instalación

Copia la carpeta de la skill donde tu agente busque skills. Con Claude Code:

```bash
git clone https://github.com/samuelurones28/seosindrama-skills.git
cp -r seosindrama-skills/skills/traducir-a-cliente ~/.claude/skills/
```

Todas las rutas (Claude Code, Codex, Cursor, clon completo) en
[`docs/instalacion.md`](docs/instalacion.md).

## Ejemplo de uso

Con `traducir-a-cliente` instalada, en Claude Code:

> Explícale a mi cliente este aviso de PageSpeed: "Reduce unused JavaScript —
> Potential savings of 3,281 KiB, est. 6,020 ms. Three chunks from
> https://www.youtube.com/... (YouTube player)". Es una web de servicios, el
> cliente no es técnico.

Respuesta:

> **Hay 3.281 KB de código descargado que no se aprovecha**
> Prioridad: alta
>
> **Qué supone para el negocio:** Descargar código innecesario puede
> retrasar la aparición del contenido y mantener ocupado el dispositivo
> durante más tiempo, especialmente con conexiones o equipos limitados. El
> ahorro de 6.020 ms es una estimación de Lighthouse, no una mejora
> garantizada ni una pérdida medida de visitantes.
>
> **Explicado de forma sencilla:** Es como transportar una caja enorme para
> entregar solo unos pocos documentos: el viaje tarda más y se consume más
> esfuerzo del necesario.
>
> **Cómo resolverlo:**
> 1. Confirma si las tres referencias a https://www.youtube.com/... corresponden
>    al reproductor de YouTube y si todas se necesitan al abrir la página.
> 2. Carga el reproductor solo cuando el visitante lo solicite, y divide o
>    retrasa el código que no participa en la primera pantalla.
> 3. Repite la auditoría y verifica que disminuyen los 3.281 KB de código no
>    utilizado y el tiempo estimado de 6.020 ms.
>
> ```
> Nota para el desarrollador: Analiza el bundle con Chrome DevTools Coverage
> o Lighthouse; aplica carga diferida y división de código. No modifiques el
> recurso servido por YouTube: controla su inclusión desde la página.
> ```

Ese hallazgo es real, generado por el mismo prompt en una auditoría de
seosindrama.com (dominio anonimizado).

## De dónde salen los datos

Las reglas, umbrales, analogías y prioridades de estas skills no salen de la
teoría sino de 731 auditorías sobre 573 dominios de pymes españolas (marzo a
septiembre de 2026). Lo que falla, en qué proporción, y las limitaciones de
la muestra están en [`docs/datos.md`](docs/datos.md).

Resumen: la web típica de una pyme aprueba (nota media 78,6) pero arrastra
dos o tres problemas concretos. El 75 % tiene un hallazgo de velocidad, el
44 % de JavaScript no usado, el 34 % de accesibilidad.

## Cómo contribuir

- **Hallazgos y errores:** abre un issue con la entrada que le diste al
  agente y lo que devolvió.
- **Nuevos términos para el glosario, nuevos tipos de negocio para el
  schema, nuevos user-agents:** pull request sobre el archivo de
  `references/` correspondiente, con fuente.
- **Nuevas skills:** abre un issue antes de escribirla para acordar el
  alcance. Cada skill necesita una sección "Qué NO hace".

Las cifras de `docs/datos.md` se actualizan desde la base de datos de
seosindrama.com; no se aceptan PR que las cambien a mano.

## Licencia

MIT. Puedes usar, copiar y modificar las skills en proyectos propios o de
clientes. Los ejemplos están anonimizados; si encuentras algún dato que
identifique a un negocio real, abre un issue y se retira.
