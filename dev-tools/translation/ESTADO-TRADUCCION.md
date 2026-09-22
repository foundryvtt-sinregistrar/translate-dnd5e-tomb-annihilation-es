# Estado de la traducción

Actualizado: 22 de septiembre de 2026.

## Estado actual

**Borrador integral con validación técnica; revisión lingüística en curso.**
No se considera una traducción final revisada.

- Cinco packs originales exportados mediante la API de Foundry, con SHA-256.
- 698 documentos principales: 1 aventura, 332 actores, 301 objetos,
  44 tablas y 20 macros.
- Adventure contiene 475 actores, 79 diarios (1.033 páginas), 42 escenas
  y 41 carpetas. Se cubren también modificaciones locales de fichas de escena.
- 20.154 campos de texto inventariados, todos con valor en la traducción.
  Los fragmentos técnicos y nombres propios pueden permanecer iguales.
- 126 claves de interfaz traducidas manualmente, conservando los parámetros.
- Glosario inicial y equivalencias contrastadas con la edición española.
- Reutilización de traducciones locales solo con coincidencia del original inglés.
- El resto se ha generado con OPUS-MT local y se mantiene identificado como borrador.

Consultar [el inventario](INVENTARIO.md), [el glosario](GLOSARIO.md) y
[el procedimiento reproducible](README.md).

## Referencias

Se han incorporado como fuentes locales las ediciones española (259 páginas)
e inglesa (260 páginas). El texto de consulta está en
`../export/data/references/es/` y `../export/data/references/en/`.

Cada idioma dispone de texto completo, archivos por página, JSONL y manifiesto
de cobertura. Se conserva la extracción nativa. Tras detectar corrupción
adicional, se ha aplicado OCR a las 259 páginas españolas y a 6 inglesas.
Los manifiestos enumeran las páginas
que requieren revisión. La numeración corresponde a la posición física en
cada PDF, no necesariamente a la página impresa.

Consultar [la guía de referencias](../export/README.md) antes de reutilizar el
contenido. Hay errores de reconocimiento y capitulares omitidas: el resultado
no constituye una transcripción revisada ni una alineación bilingüe.

Los PDF y las extracciones permanecen en la carpeta local excluida de Git.

## Validación y correcciones

- Auditoría de cobertura, sintaxis de Foundry, HTML y números contra los originales.
- Validación con Babele 2.9.1 y los esquemas reales de Foundry 14.368 / dnd5e 6.0.3.
- Convertidor por ID para carpetas internas de Adventure.
- Convertidor específico para actores de Adventure: evita que traducciones de
  otros compendios sustituyan nombres propios o biografías con `@Embed`.
- Convertidor de fichas que incluye los textos de sus ActorDelta.
- Piloto creado en carpetas «ToA — Pruebas de traducción»: Cuenca Aldani,
  Ataaz Muhahah, Murciélago, Rubí y Cantidad de yuan-tis malison que regresan.
- Módulo activado en el mundo de desarrollo; panel de Chult e interfaz en español.
- Resultado final: 20.154 campos aplicados, 698 documentos aceptados por Foundry,
  cero errores de mapeo o cambios mecánicos y 18 pruebas automatizadas superadas.
  El diario piloto se ha abierto en la interfaz y conserva texto, enlaces y tirada.

Los informes de ejecución y las instantáneas están en `../export/data/`.
Consultar [el resumen de validación](VALIDACION.md).
La creación de estos cinco documentos no equivale a importar toda la aventura.

## Revisión editorial por lotes

### intro-01 — Prefacio, introducción y resumen de la historia

- Rama de trabajo: `develop`.
- Revisadas tres páginas del diario `toaIntroduction0`: seis campos (título y
  texto de cada página). El resto del diario sigue pendiente.
- Referencias: extracción española de las páginas físicas 3 y 6, contrastada
  con el texto inglés exportado de Foundry. No se ha realizado una comprobación
  visual de estas páginas del PDF en este lote.
- Corregidos errores de sentido, género y nombres: Chult como territorio
  tropical, Syndra y Valindra en femenino, Arpistas, Plaga de Conjuros,
  Fano de la Serpiente Nocturna y archiliche Acererak, entre otros.
- Conservados los enlaces de Foundry, las etiquetas HTML y las cifras.
  Se mantiene la identificación explícita «yuan-ti malison» del original inglés
  y la ubicación de la tumba bajo la ciudad.
- Textos registrados en `reviewed-segments.json`; rutas y huellas de los seis
  campos en [el registro editorial](editorial-review.json). Se retiraron sus
  entradas de la procedencia automática local.
- Auditoría estática posterior: cero campos ausentes y cero discrepancias de
  sintaxis, HTML o números en los 20.154 campos del módulo.
- Las instantáneas de Babele anteriores a este lote no validan estas nuevas
  redacciones. Su comprobación visual en Foundry queda pendiente.

Commit del primer lote: `e7d2a12` — `Review introduction prose against Spanish reference`.

### intro-02 — Dramatis personae

- Revisados el título y el texto de la página `QmPzaqUnuohBRwfU`: 48 filas de PNJ,
  con nombres, pronunciaciones y descripciones.
- Referencias: página física 5 del PDF español, comprobada visualmente, y texto
  inglés exportado de Foundry. Se conserva el orden de filas del original inglés.
- Corregidos nombres como Saco de Clavos, Jarro de Vino, Bruma del Río,
  Pillapincha, Mustio y Salysa; restaurados apóstrofos y acentos dañados.
- Corregidas las descripciones de criaturas, profesiones, géneros y servicios
  mercantiles. Pronunciaciones adaptadas a las de la edición española.
- Conservados los 47 UUID de actores, las tres columnas y todo el marcado HTML.
  Na conserva la indicación «no combatiente»; Qawasha conserva su función de guía.
- Dos campos registrados con sus huellas en `editorial-review.json` y sus
  equivalencias completas en `reviewed-segments.json`. No se han sustituido
  automáticamente los nombres en otros documentos.
- Auditoría de los 20.154 campos: cero ausencias y cero discrepancias de sintaxis,
  HTML o cifras. La comprobación visual de la tabla en Foundry queda pendiente.

Commit de `intro-02`: `8b6bf18` — `Review Dramatis Personae names and descriptions`.

### intro-03 — Dirigir la aventura: indicaciones generales y abreviaturas

- Revisado el título y el fragmento inicial de `YmJBk6SpQqatzqxa`, hasta el final
  de las abreviaturas. **La página completa sigue parcialmente revisada.**
- Referencias: extracciones españolas de las páginas físicas 6 y 7, contrastadas
  con el original inglés de Foundry. Sin comprobación visual del PDF en este lote.
- Corregidas las instrucciones de lectura en voz alta, las referencias a los
  perfiles y los manuales, y las 19 abreviaturas de reglas, monedas y alineamientos.
- Se usan «pg», «CA», «CD», «PX», «ppt», «po», «pe», «pp» y «pc», con los
  significados de la edición española. Se conserva el orden de los párrafos.
- El primer párrafo mantiene los dos manuales enumerados por Foundry; el PDF
  enumera tres. Se conserva también la mención posterior a la Guía del Dungeon
  Master. Los títulos de los manuales se presentan en español.
- Se conservan los tres UUID, la clase `fvtt narrative` y el diseño de las
  abreviaturas. El resto de la página no se ha modificado.
- El registro editorial delimita el fragmento mediante el encabezado de la
  sección siguiente; sus huellas corresponden solo a ese fragmento. Se conserva
  la equivalencia parcial en `reviewed-segments.json`, sin registrar como revisado
  el texto completo. Se retiró la huella automática local de este campo mixto;
  esa retirada no acredita la revisión de las secciones restantes.
- Auditoría de los 20.154 campos: cero ausencias y cero discrepancias de sintaxis,
  HTML o cifras. Comprobación visual en Foundry pendiente.

Commit de `intro-03`: `86041ba` — `Review adventure guidance and rules abbreviations`.

### intro-04 — Resumen de la aventura y ¿Quién es Acererak?

- Revisadas ambas secciones de `YmJBk6SpQqatzqxa`, desde «Resumen de la aventura»
  hasta el final del recuadro sobre Acererak. El resto de la página no se modifica.
- Referencias: extracción española de la página física 7 y original inglés de
  Foundry. Se ha reconstruido el orden de lectura de las columnas con el original
  inglés; no se ha realizado una comprobación visual del PDF en este lote.
- Corregidos el recorrido por los capítulos, las pistas sobre Omu, los nombres de
  informantes y embarcaciones, y el relato de Acererak, su filacteria y el atropal.
  Se aplican Salysa, Zalkore, Yaya Pu’pu, Narval y Diosa Estelar en su contexto.
- Conservados los 24 enlaces UUID en su orden original, los encabezados y el
  recuadro `aside.notable`. No cambian cifras ni contenido mecánico.
- Fragmento registrado en `editorial-review.json` con límites de inicio incluido
  y final excluido, y en `reviewed-segments.json` como equivalencia parcial.
- Auditoría de los 20.154 campos: cero ausencias y cero discrepancias de sintaxis,
  HTML o cifras. La página continúa parcialmente revisada y queda pendiente su
  comprobación visual en Foundry.

Siguiente lote: «Maldición de muerte», incluidas sus reglas y las indicaciones
específicas de Foundry. Después, «Picadora de carne», «Devorar almas» y las
secciones restantes sobre personajes y ritmo de la aventura.

## Trabajo que sigue pendiente

- Revisar editorialmente el borrador contra el PDF, por capítulos y apéndices.
  La generación automática contiene expresiones poco naturales y puede cometer
  errores de sentido que las comprobaciones técnicas no detectan.
- Revisar nombres, terminología en contexto y etiquetas dentro de imágenes.
- Validar una importación completa de Adventure en un mundo limpio y comprobar
  las automatizaciones durante el juego. No sobrescribir el mundo existente.
- Preparar la publicación únicamente después de cerrar estas revisiones.

Todavía no se ha publicado una versión instalable con estos cambios.
