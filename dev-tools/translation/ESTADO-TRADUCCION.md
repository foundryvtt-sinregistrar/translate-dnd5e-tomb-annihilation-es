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

Commit de `intro-04`: `91c81ab` — `Review adventure summary and Acererak background`.

### intro-05 — Final de Dirigir la aventura

- Revisado todo el texto restante: maldición de muerte, picadora de carne,
  devorar almas, personajes de repuesto, cuenta atrás, avance y niveles superiores.
- Referencias españolas: páginas físicas 7-9. Se conserva lo revisado en los
  lotes anteriores (páginas 6-7); el registro incluye ahora la huella completa
  de la página de Foundry, además de las huellas históricas de sus fragmentos.
- Revisadas las condiciones y negaciones, la reducción diaria de puntos de golpe,
  los resultados de d20, los umbrales de salvación y la tabla de niveles y PX.
- Los dos avisos exclusivos de Foundry se traducen desde el original inglés.
  Conservados sus destinos, iconos y clases, y los 22 UUID del bloque nuevo.

### intro-06 — Empezar la aventura

- Revisada la página completa con las referencias de las páginas físicas 9-11:
  presentación de Syndra, diálogo, recompensa, mapa, teletransporte y 15 ganchos.
- Conservados 79 puntos de golpe, pérdida diaria de 1, límite de 0, anticipo
  de 50 po por personaje, rarezas y los diez enlaces originales.
- Se preservan los añadidos y omisiones de Foundry respecto del texto impreso,
  sin añadir referencias a páginas o mapas físicos que no aparecen en el original.
- Auditoría estática sin errores. `audit_editorial.py` comprueba las huellas
  tanto del original inglés como de la traducción, incluidos los lotes parciales.
- Los seis textos del diario de introducción tienen revisión lingüística;
  sigue pendiente la comprobación visual en Foundry y la portada es un recurso
  gráfico cuyo texto integrado no se ha traducido.

Commit de `intro-05` y `intro-06`: `ab70dfa` —
`Complete editorial review of adventure introduction text`.

### ch1-01 a ch1-38 — Diario principal Puerto Nyanzaru

- Revisados los títulos y textos de las 38 páginas de `toaCh1PortNyanza`, usando
  las referencias españolas de las páginas físicas 16-17, 19, 25-28 y 30-37.
- Cobertura: llegada, orientación urbana, habitantes, facciones, príncipes,
  Volo, comercio, carreras de dinosaurios, contratación de guías y los nueve
  grupos de guías. Se conserva el formato de los avisos exclusivos de Foundry.
- Los siete resúmenes de príncipes conservan sus `@Embed`. La revisión de estas
  páginas no acredita la revisión de las biografías de actores que insertan.
- Se conserva la numeración de documentos de Foundry, que difiere del PDF español
  para varios guías. También se conservan las omisiones del original de Foundry,
  como algunos detalles de Bruma y Gondolo, y las unidades originales.
- Se corrigen sentidos frente al PDF cuando lo exige el inglés: la lona del
  colector mide 5 pies de lado, los ataques en carreras se permiten con una
  diferencia de 50 o menos, y el libro de Volo se sustituye por el apéndice D
  cuando no está disponible el libro de consulta.
- Los nueve pagos de apuestas conservan exactamente sus operadores de división
  y multiplicación. Las tablas mantienen estadísticas, tiradas y destinos.
- Se unifica «Barrio del Puerto» para Harbor Ward; el PDF alterna barrio/distrito.
- 90 registros editoriales verificados contra EN y ES; auditoría de los 20.154
  campos sin errores. Sin nueva validación visual en Foundry.
- **El capítulo 1 no está completamente revisado**: faltan localizaciones,
  villa, misiones secundarias y contenido insertado de fichas y tablas.

Commit del diario principal: `958a925` — `Review all main Port Nyanzaru journal pages`.

### ch1-quests-01 a ch1-quests-11 — Misiones secundarias

- Revisadas las once páginas de `toaCh1SideQuests`: introducción y diez misiones.
  Referencias españolas de las páginas físicas 17-18.
- Corregidos personajes, objetivos, consecuencias y recompensas sin cambiar
  condiciones, plazos, monedas ni enlaces. Summerwise se traduce como Estival.

### ch1-villa-01 a ch1-villa-19 — Villa de un príncipe mercante

- Revisadas las diecinueve páginas de `toaCh1MerchantPr`, con referencias de las
  páginas físicas 28-30: decoración, plantas, habitaciones, guardias y tesoro.
- Conservados el mapa insertado, los enlaces relativos, estadísticas y tiradas.
  La anotación inglesa dentro del comando de tirada del joyero se conserva como
  parte del token técnico; no se considera traducido ese comentario de tirada.

### ch1-locations-01 a ch1-locations-32 — Localizaciones de la ciudad

- Revisadas las 32 páginas de `toaCh1LocPortNya`, con referencias españolas de las
  páginas físicas 19 y 21-25. El mapa de la página 20 no se modifica.
- Corregidos barrios, templos, comercio, transporte y descripciones narrativas.
  Se mantienen Goldenthrone y los nombres oficiales españoles de lugares.
- Se conserva la vela mayor cuadra indicada por el original inglés, aunque la
  referencia española dice cangreja. El presagio de Savras trata del futuro de
  recién nacidos, no de su aspecto físico. Las referencias técnicas siguen intactas.

### ch1-prince-actors-01 — Biografías de los príncipes mercantes

- Revisadas las siete biografías completas, nombres y nombres de ficha en el
  compendio de actores y en la aventura: 42 campos. Referencias españolas de
  las páginas físicas 26-28, contrastadas con cada original inglés.
- Corregidos relaciones, negocios, precios, servicios, maldición de Jessamine
  y recompensa de Wakanga. Se mantienen los destinos propios de cada copia,
  el enlace sin destino de Ekene-Afa en el pack y la tirada de la aventura.
- La revisión de las biografías no incluye las acciones ni los objetos de las
  fichas. Auditorías técnica y editorial sin errores; sin comprobación visual.

### ch1-tables-equipment-01 — Rumores, encuentros urbanos y yklwa

- Revisados los 19 rumores de Chult (página física 37), los once encuentros
  urbanos (194) y la descripción de la yklwa (33), además de sus nombres.
  Se registran 36 campos, incluidas las coincidencias exactas del nombre Yklwa.
- Se conserva el carácter de rumor, con sus posibles inexactitudes. La bruma
  provoca alucinaciones mágicas según el inglés. Se mantienen todas las tiradas,
  recompensas, distancias y destinos; no se añaden conversiones métricas.
- No incluye la revisión de las imágenes de documentos de los guías ni de los
  atributos y acciones de los actores que pueden aparecer en estos encuentros.
- Auditorías técnica y editorial sin errores.

### ch2-travel-01 a ch2-travel-12 — Viaje por las tierras de Chult

- Revisados los doce títulos y textos de `toaCh2TheLandOfC`: preparación,
  distancias, orientación, deshidratación, enfermedades, Artus y Dragonbait,
  encuentros y territorios de muertos vivientes. Referencias físicas 38-39 y 41-42.
- Conservados los ritmos, bonificadores y penalizaciones, las salvaciones,
  condiciones de recuperación y funciones propias de Foundry.
- `Blue Mist Fever` se traduce como «Fiebre de la bruma azul»: el original de
  Foundry tiene alucinaciones de monos azules y salvaciones cada 24 horas, en
  lugar de las reglas de locura de «Fiebre del mono loco» del PDF español.
- Para las sanguijuelas, fallar la salvación aumenta el cansancio y superarla
  lo reduce. Se corrige la inversión que contiene el PDF español según el inglés.
- Auditorías técnica y editorial sin errores. El arte y mapa insertados no se
  han modificado ni se consideran revisados por esta revisión del texto.

### ch2-sites-01 a ch2-sites-08 — Cuenca, gargantas y Bahía de Chult

- Revisados ocho textos y sus títulos: Cuenca Aldani, Ataaz Kahakla, las cuatro
  páginas de Ataaz Muhahah, Ataaz Yklwazi y Bahía de Chult. Referencias físicas
  42-44 y 52. Corregidas narración, instrucciones y etiquetas de enlaces.
- Conservadas condiciones del gólem, distancias de salto, patrullas y tributo
  de Aremag. Las ayudas de Foundry se traducen desde el original de la exportación.
- Detectada una discrepancia técnica original en el tributo de Aremag:
  `[[/gmr 2d4*20]]{2d4 × 50}` muestra una cantidad distinta de la que tira.
  El PDF español respalda ×50. Se conserva el comando original durante la
  revisión lingüística; queda pendiente resolver esta incidencia técnica antes
  de publicar. Las auditorías de preservación no detectan errores del original.
- Auditorías técnica y editorial sin errores introducidos por la traducción.

### ch2-righteous-01 a ch2-righteous-12 — Campamento Justicia

- Revisadas las doce páginas del diario completo con las referencias físicas
  45-48: campamento, goblins, dependencias, leyenda y cinco zonas del santuario.
- Aclaradas las reglas de ir a hombros, los umbrales de las pruebas, los patrones
  de cuatro por cuatro, las trampas y el transporte de la vasija alquímica.
- En la escalera ambos personajes caen solo si ambos fallan sus pruebas,
  conforme al inglés. Se conservan los daños, probabilidades, salvaciones,
  enlaces relativos y avisos de automatización de Foundry.
- Los comentarios ingleses internos de las tiradas se conservan como tokens
  técnicos. Algunos dicen «resultado de 1» aunque la fórmula comprueba ≤50;
  es otra incoherencia del original, no una traducción validada de esos comentarios.
- Auditorías técnica y editorial sin errores introducidos por la traducción.

## Balance de revisión editorial

- 138 páginas de texto revisadas: seis de la introducción, cien de los cuatro
  diarios del capítulo 1 (38 + 11 + 19 + 32), doce de reglas de viaje y veinte de
  localizaciones del capítulo 2. No equivale a 138 páginas del PDF.
- 356 registros editoriales comprobados contra originales y traducciones,
  incluidos los registros históricos parciales; no son 356 campos distintos.
- La revisión de un diario con `@Embed` no acredita el contenido del documento
  insertado. Salvo las siete biografías de los príncipes, faltan las biografías,
  objetos, tablas, ayudas, escenas e interfaz
  relacionadas, además de los capítulos 2-5 y los apéndices.
- Auditorías estáticas y editorial sin errores. No se han renovado las
  instantáneas de Babele ni realizado una importación completa de Adventure.
- **La revisión del módulo continúa incompleta.** El siguiente trabajo es revisar
  los contenidos insertados del capítulo 1 y seguir con el capítulo 2.

## Trabajo que sigue pendiente

- Revisar editorialmente el borrador contra el PDF, por capítulos y apéndices.
  La generación automática contiene expresiones poco naturales y puede cometer
  errores de sentido que las comprobaciones técnicas no detectan.
- Revisar nombres, terminología en contexto y etiquetas dentro de imágenes.
- Validar una importación completa de Adventure en un mundo limpio y comprobar
  las automatizaciones durante el juego. No sobrescribir el mundo existente.
- Preparar la publicación únicamente después de cerrar estas revisiones.

Todavía no se ha publicado una versión instalable con estos cambios.
