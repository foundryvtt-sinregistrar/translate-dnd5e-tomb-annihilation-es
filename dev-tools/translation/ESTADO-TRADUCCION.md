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

### ch2-vengeance-01 a ch2-vengeance-09 — Campamento Venganza

- Revisadas las nueve páginas y sus títulos con referencias físicas 48-50:
  guarnición, suministros, puerta, atalayas, enfermería, mando, tiendas y letrinas.
- Corregidos funciones de los oficiales, coberturas y condiciones de las órdenes
  de Breakbone. La enfermedad se denomina «fiebre de la bruma azul» como en las
  reglas de viaje revisadas. Se conservan efectivos, plazos, pruebas y destinos.
- Auditorías técnica y editorial sin errores. Las fichas de los PNJ y la escena
  no quedan acreditadas como revisadas por la revisión de este diario.

### ch2-dungrunglung-01 a ch2-dungrunglung-08 y tabla — Dungrunglung

- Revisados los ocho títulos y textos del diario y los nueve resultados y título
  de la tabla del laberinto espinoso. Referencias físicas 55-58.
- Corregidos motivaciones y lealtades, audiencias, encarcelamiento, cuatro pruebas
  del Gran Ritual y consecuencias. Roark admite ayuda contra los muertos vivientes;
  se corrige el sentido ambiguo de la referencia española conforme al inglés.
- Conservada la numeración de mapas de Foundry (2.5 frente a 2.7 del PDF), las
  cantidades, tiradas, UUID y los añadidos de automatización.
- Pendiente en la comprobación visual: los saltos a encabezados con fragmentos
  como `#grungs-of-dungrunglung` y las etiquetas inglesas dentro de `@Embed`.
  Preservar el token original no acredita por sí solo su navegación o presentación.
- Auditorías técnica y editorial sin errores; no se han revisado aún las fichas
  de los grungs ni las imágenes insertadas.

### ch2-firefinger-01 a ch2-firefinger-06 — El Caldero y Dedo de Fuego

- Revisados El Caldero y las cinco páginas de Dedo de Fuego con referencias
  físicas 53-55 y 58: aproximación, escalada, cuevas, Nephyr, pináculo y tesoros.
- Se aclaran la prueba de grupo y las condiciones de detección, caída y daño.
  La cima mide unos 40 pies de lado, según el inglés, no 40 pies cuadrados.
- Se conserva la identidad femenina de la exploradora de la cueva de estirges,
  la escalera hacia el tercer nivel omitida en el PDF y las recompensas de Nephyr.
- Auditorías técnica y editorial sin errores; comentario interno de la tirada
  de viento conservado en inglés. No incluye las fichas ni el mapa.

### ch2-short-sites-01 a ch2-short-sites-21 — Geografía y localizaciones breves

- Revisados 21 textos y títulos: Hisari, Ishau, Bahía Jahaka, Ensenada de Kitcher,
  Lago Luo, Tierra de Humo y Ceniza, Barranco Brumoso, Desierto Nsi, Omu, Puerto
  Castigliar, Bahía Refugio, los cuatro ríos, Shilku y su bahía, Hocico de Omgar
  y los valles del Terror, Ascuas y Honor Perdido. Referencias físicas 44-45,
  55, 58, 65-66, 70, 74, 85, 87 y 89-90.
- Corregidas direcciones y relaciones geográficas. Las 40 millas de Bahía Jahaka
  expresan su extensión tierra adentro, no una profundidad vertical. Las cascadas
  del Soshenstar están a lo largo del río, no después de desembocar en la bahía.
- En Desierto Nsi se conserva una docena de tortugas, como en el inglés, frente
  a las decenas del PDF. En Tierra de Humo y Ceniza se conservan 20-40 grados
  Fahrenheit sin introducir la conversión métrica del PDF.
- Auditorías técnica y editorial sin errores.

### ch2-beluarian-01 a ch2-beluarian-21 — Fuerte Beluarian

- Revisados los 21 textos y títulos del diario con referencias físicas 61-65:
  Liara, guarnición, permisos, tres misiones, comercio y todas las dependencias.
- Conservados los 50 po del permiso, el reparto de ganancias, las recompensas,
  los recargos comerciales y las condiciones de cada misión. Se corrigen a una
  docena los comerciantes del bazar según el inglés, frente a media docena del PDF.
- Diferenciadas las doce ocasiones diarias en que se toca la campana del número
  de campanadas de cada turno. Se reparan paréntesis mal colocados en etiquetas
  visibles, manteniendo los UUID y comandos originales.
- Incidencia original pendiente: el enlace a «Agentes del Puño Ardiente» desde
  el salón apunta a la página del campo de justas (`fvechDnR8pzjwGbc`), aunque el
  recuadro está en la introducción (`HWmjK7tPH3WrZzrg`). Se conserva el destino
  original en esta revisión; debe resolverse en la validación de navegación.
- Auditorías técnica y editorial sin errores introducidos por la traducción.

### ch2-heart-01 a ch2-heart-07 — Corazón de Ubtao

- Revisadas las siete páginas y sus títulos con referencias físicas 50-52:
  Valindra, árbol, escalera, entrada, guarida, guardianes y teletransporte.
- Se mantienen los 200 pies de altura del inglés frente a los 100 del PDF,
  el mapa 2.8 de Foundry y todas las condiciones de la ilusión de Valindra.
- Corregido el sentido de la pendiente: asciende hacia dentro y permite que el
  agua salga. Conservados objetivos, conjuros y tesoros. Commit: `b189e78`.

### ch2-mezro-vorn-toba-01 a ch2-mezro-vorn-toba-03 — Mezro, Vorn y Rey Toba

- Revisadas las páginas completas de Mezro, Bahía Tortuga Mordedora y Vorn,
  con sus títulos. Referencias físicas 45, 76 y 90.
- Aclarados el destino de Mezro y la promesa de Alisanda, los incentivos de los
  cíclopes, las defensas del Rey Toba y las consecuencias de llevarse a Vorn.
- Se mantiene «fiebre de la bruma azul» en Vorn, conforme a las reglas de Foundry.
- Ambos bloques pasan las auditorías técnica y editorial. Las fichas e imágenes
  no se consideran revisadas por la revisión de estos diarios.

### ch2-yellyark-01 a ch2-yellyark-07 — Yellyark

- Revisadas las siete páginas y sus títulos con referencias físicas 90-91:
  vigilancia, dependencias, reina Pillapincha, amuleto, hormigueros y lanzamiento.
- Las mil yardas describen el desplazamiento de la aldea, no una altura vertical.
  Los goblins no viajan dentro de ella; se conservan daños y defensas de la liana.
- Traducidas desde el inglés las instrucciones para usar la torre de combate
  como actor de grupo. No acreditan una comprobación de su funcionamiento en juego.
- Incidencia original: el enlace del aviso «Activar la escena Yellyark» apunta
  al diario `JournalEntry.toaCh2Yellyark00`, no a la escena. Destino conservado
  en esta revisión y pendiente de la validación de navegación.
- Auditorías técnica y editorial sin errores introducidos por la traducción.

### ch2-explorers-01 a ch2-explorers-03 — Hvalspyd, Huesos de Aguja y Narval

- Revisados los tres textos completos y sus títulos con referencias físicas
  69-70 y 88-89. Se conservan las reglas, cifras y enlaces de Foundry.
- Hvalspyd desembarca en Bahía del Refugio. En Huesos de Aguja se conserva
  la CD 13 del original inglés, frente a la CD 15 del PDF español.
- En el Narval se corrige «tronco» por «baúl» y se aclaran la ventilación,
  la tirada de encuentro, el parentesco de Bwayes y la hostilidad condicional.
- Auditorías técnica y editorial sin errores.

### ch2-mbala-01 a ch2-mbala-05 — Mbala

- Revisados los cinco textos y sus títulos contra el inglés y las páginas
  físicas 74-76 del PDF español: acceso, Yaya Pu’pu, ritual, tesoro y nido.
- Corregidos el ascenso en zigzag, los cien pies hasta el borde superior,
  la tumba del gólem fuera de la choza y la daga plateada del tesoro.
- Aclarados el espíritu que imita al fallecido y el deterioro irreversible
  del cuerpo. Se mantienen las reglas, cifras, UUID y estructura de Foundry.
- Auditorías técnica y editorial sin errores.

### ch2-orolunga-01 a ch2-orolunga-06 — Orolunga

- Revisados los seis textos y sus títulos con referencias físicas 85-87:
  zigurat, tres pruebas, audiencia con Saja N’baza y salida del santuario.
- Conservados los objetos necesarios, el daño por avance, la desventaja por
  alineamiento, el aumento de CD por fallo y la única oportunidad de audiencia.
- Corregida la etiqueta visible truncada «Saja N’baz» a «Saja N’baza».
- La altura total aproximada de 60 pies y los desniveles de 30, 20 y 12 pies
  proceden del original; se conservan sin armonizar sus cifras.
- Auditorías técnica y editorial sin errores.

### ch2-star-goddess-01 a ch2-star-goddess-04 — Diosa Estelar

- Revisados los cuatro textos y sus títulos contra el inglés y las páginas
  físicas 87-88: naufragio, supervivientes, carroñeros y suministros recuperables.
- Conservados el mapa 2.13 de Foundry, las alturas relativas de las secciones,
  los cuatro niveles de cansancio y las condiciones de movimiento y caída.
- Ra-das se describe como navegante; el globo contiene gas más ligero que el
  aire. Traducido también el aviso de activación de escena propio de Foundry.
- Auditorías técnica y editorial sin errores; no acredita revisión de fichas.

### ch2-jahaka-01 a ch2-jahaka-10 — Fondeadero de Jahaka

- Revisados los diez textos y sus títulos contra el inglés y las páginas
  físicas 58-61: base, tres tripulaciones, defensas y todas las dependencias.
- Corregidos los aposentos sucios (no los tripulantes), los cofres sin cerrar
  con llave, las mesas de la taberna y los numerosos clientes de Laskilar.
- Conservadas las dos condiciones independientes de las espadas: no atacan a
  criaturas con parche ni se animan cuando estas manipulan el tesoro.
- Se mantienen el nombre Kalita sin el epíteto del PDF, el mapa 2.10 de Foundry,
  la escala de escena de 5 pies y las instrucciones sobre teletransporte.
- Eliminada una llave de cierre sobrante del texto visible de Ojo de las
  Profundidades. Los UUID, comandos, cifras y etiquetas HTML se conservan.
- El enlace original con fragmento `#pirates-of-jahaka-anchorage` se conserva;
  su navegación al encabezado traducido queda pendiente de validar en Foundry.
- Auditorías técnica y editorial sin errores. La revisión de las biografías
  del recuadro no acredita la revisión de sus fichas de actor.

### ch2-hrakhamar-01 a ch2-hrakhamar-11 — Hrakhamar

- Revisados los once textos y títulos con referencias físicas 66-69: llegada,
  fundición, fragua, tesoro, capilla, humo, prisioneros y vagonetas.
- Conservados el mapa 2.9 de Foundry y los cinco niveles de cansancio de los
  prisioneros, frente a los tres del PDF español. Las precauciones contra el
  humo duran diez asaltos; los caminantes se liberan en cada asalto sucesivo.
- Aclaradas las tres condiciones de activación de la trampa y que se repliega
  la pasarela. Traducidas las instrucciones de sus macros sin modificar UUID.
- Corregidos la fundición como estancia, el depósito de vagonetas y el plural
  visible de martillos de guerra. Se conservan cifras, comandos y estructura.
- Auditorías técnica y editorial sin errores. Las macros no se han probado
  en una sesión de juego y las fichas insertadas no se consideran revisadas.

### ch2-wyrmheart-01 a ch2-wyrmheart-17 — Mina Wyrmheart

- Revisados los diecisiete textos y títulos con referencias físicas 77-80:
  entrada, vagonetas, kobolds, trampas, audiencias y guarida de Yesca.
- Corregidas según el inglés la huida ascendente de los urds y la desventaja
  de Yesca en Percepción por la cascada. La ventaja para quienes se esconden
  depende de quedar fuera de la vista desde la guarida, no de estar dentro.
- Aclarado que la cantidad aleatoria de equipo del tesoro corresponde a cada
  tipo de objeto, no a cada caja. Se conservan el mapa 2.14 y las reglas de
  caída, frenado, daños, CA y efectos de las trampas de Foundry.
- Traducidas las instrucciones de la región y la macro del tronco oculto.
  Incidencia original: los comentarios de las tiradas de frenos y del tronco
  dicen «on a result of 1» o «on a 1», pese a usar d100 con umbrales 10 o 50.
  Comandos conservados; discrepancia pendiente de la validación técnica.
- Auditorías técnica y editorial sin errores; no se ha probado la escena
  ni se acredita la revisión de los actores o los objetos enlazados.

### ch2-kir-sabal-01 a ch2-kir-sabal-16 — Kir Sabal

- Revisados dieciséis textos y títulos con referencias físicas 71-74: ascenso,
  habitantes, ritual, herederos de Omu y dependencias del monasterio.
- Conservadas las condiciones de vuelo y ascenso, los motivos de Asharra,
  las recompensas y la retirada de las gárgolas. Corregidos términos de
  arquitectura, mobiliario, tutela y etiquetas visibles de los enlaces.
- Incidencias del original pendientes de validación: el texto de Asharra
  anuncia un atributo de conjuros «más abajo», pero no lo desarrolla en el
  diario; la casa real tiene una etiqueta `a` sin destino para la zona 4;
  el ritual usa un fragmento inglés que debe comprobarse con el título traducido.
- Auditorías técnica y editorial sin errores. Las fichas y las imágenes
  insertadas no quedan acreditadas por esta revisión del diario.

### ch2-nangalore-01 a ch2-nangalore-13 — Nangalore

- Revisados trece textos y títulos con referencias físicas 80 y 82-85:
  historia de Zalkoré, inscripciones, jardines, palacio y audiencia.
- Conservadas las salvaciones cada hora del original inglés, frente a cada
  turno en el PDF. Corregidos la petrificación de Gowl, «ahora adorno» y la
  imposibilidad de expulsar al espíritu de Thiru-taya. El vestido se arruina
  cuando más de la mitad del daño es de los tipos indicados, no exactamente la mitad.
- El inglés exportado omite el comparador de Percepción pasiva: se explicita
  «no alcance» el umbral de 12, conforme al PDF, manteniendo el comando.
- Se conserva el mapa 2.12 y la estatua de 18 pies del inglés. La alternativa
  de entregar un personaje por la orquídea no figura en este original de Foundry.
- Incidencia original: el orden indicado para alternar las caras no coincide
  con su numeración y orientación. Se conserva y queda pendiente de comprobación
  con el mapa. Eliminado un paréntesis mal ubicado en el enlace al capítulo 1.
- Auditorías técnica y editorial sin errores. La tabla de descubrimientos
  insertada y las fichas de criaturas quedan fuera de este bloque.

### ch2-location-index-00 a ch2-location-index-48 — Índice de Chult

- Revisadas la descripción general y las 48 tarjetas de localizaciones,
  incluidos títulos, resúmenes, tipos de encuentro e instrucciones del mapa.
- Estos resúmenes proceden del contenido específico de Foundry: sus registros
  declaran revisión contra el exportado inglés, sin atribuirlos al PDF español.
- Corregidos Dedo de Fuego, el nombre truncado de Ataaz Yklwazi, Narval,
  las etiquetas visibles y la terminología recurrente. Se conservan iconos,
  destinos y estructura. Se aclara que el orden alfabético es el del original.
- Las tarjetas simplifican o amplían algunos diarios originales; por ejemplo,
  el resumen de Campamento Justicia habla de apariciones y el del Caldero usa
  «Bahía de Humo». Se conserva el alcance de esos resúmenes y no se considera
  que añadan mecánicas a las localizaciones. Las instrucciones de permisos
  y mapa quedan pendientes de validación en la interfaz de Foundry.
- Comprobación de cobertura: todos los textos de los diarios principales del
  capítulo 2 y su índice tienen registro editorial completo. Los documentos
  enlazados, escenas y reglas adicionales conservan su estado independiente.
- Auditorías técnica y editorial sin errores.

### ch3-history-01 a ch3-history-10 — Historia y leyenda de Omu

- Revisados diez textos y títulos con referencias físicas 92-94: introducción,
  historia, caída, ascensión de Ras Nsi, leyenda y primeras facciones.
- Se conservan cronología, rivalidades, condiciones de traducción del omuense
  y emboscada de Salysa. Normalizados ranamot, sucarate, caracol flagelo,
  corrupto yuan-ti y los nombres de los nueve dioses.
- «Lidiar con» los habitantes conserva el alcance del inglés, sin convertir
  todo contacto en combate. Se distingue el destino del mundo del de Ras Nsi.
- Auditorías técnica y editorial sin errores.

### ch3-dwellers-11 a ch3-dwellers-30 — Facciones, cubos y exploración

- Revisados veinte textos y títulos con referencias físicas 92-96. Con el
  bloque histórico quedan revisadas las treinta páginas del diario de moradores.
- Conservadas las probabilidades acumulativas de los cubos y las trampas,
  los hitos de cinco y ocho cubos, la traición de Zagmira y las reglas de viaje.
- Normalizados Linterna Sorda, Saco de Clavos, Campana de Cobre y Mustio.
  Se mantiene «bruma azul» conforme a las reglas actuales del módulo.
- Incidencia original: el enlace «zona 2» de Orvex en Magos Rojos apunta a
  `1OW6XNY0uSshdsMP` (Llegada a la ciudad), no al recinto de la zona 2.
  Destino conservado y pendiente de validación de navegación. Las tablas
  insertadas conservan sus comandos, incluido `@embed` en minúsculas.
- Auditorías técnica y editorial sin errores; tablas, fichas y ayudas
  enlazadas no quedan acreditadas por revisar estos textos.

### ch3-first-shrines-01 a ch3-first-shrines-12 — Entrada y primeros santuarios

- Revisados doce textos y títulos: mapa, entrada, recinto amurallado y
  santuarios de Kubazan y Shagambi, con referencias físicas 97-98 y 101.
- Aclarados el disparador de la puerta de Kubazan, la retirada del peso de
  los travesaños, el gas y la sustitución del cubo por un peso equivalente.
- Conservadas las condiciones de victoria dentro del foso de Shagambi y
  la regeneración de gladiadores y lanzas. Corregida la edad de las crías:
  desarrollan serpientes a los seis meses y son adultas al año.
- Incidencia original: el enlace de activar escena de Shagambi apunta a
  la propia página `w4pG6tMPtjxkqscF`. Se conserva y queda pendiente de
  validación de navegación en Foundry.
- Auditorías técnica y editorial sin errores.

### ch3-moa-01 a ch3-moa-07 — Gran sima y santuario de Moa

- Revisados siete textos y títulos con referencias físicas 102-103.
- Conservados los efectos distintos de los tres cubos, el desbloqueo de los
  pozos y las inmunidades de los arqueros frente a ataques no mágicos.
- El exportado enlaza las aspilleras solo con 6D, mientras el PDF menciona
  6D y 6E. Se conserva el enlace original; requiere cotejo con el mapa.
- La instrucción de activar escena enlaza a la propia página del santuario
  `Jw1lIRKd64l8qcab`; queda pendiente de validación en Foundry.
- Auditorías técnica y editorial sin errores.

### ch3-unkh-ijin-01 a ch3-unkh-ijin-11 — Árbol caído, Unkh e I’jin

- Revisados once textos y títulos con referencias físicas 103-105, incluido
  el campamento de la Compañía del Estandarte Amarillo.
- Normalizado Ombligo de la Luna frente al «Anillo» de este pasaje del PDF,
  conforme al nombre usado en el capítulo 5. El objeto enlazado sigue pendiente.
- Aclarado que forzar mal la cerradura de Unkh activa la trampa al fallar por
  cinco o más; conservados el cuarto de vuelta y la superposición de llaves.
- Incidencia original: el suelo de I’jin mide 20 por 10 pies, pero sus treinta
  y dos losas de 5 pies de lado se distribuyen en ocho filas de cuatro.
  Se conservan las medidas del exportado; requieren cotejo con el mapa.
- El enlace de activar escena de Unkh apunta a `IaBosPPOjDC1pvv7`, la propia
  página del santuario; pendiente de validación de navegación.
- Auditorías técnica y editorial sin errores.

### ch3-wongo-01 a ch3-wongo-08 — Wongo, anfiteatro y bazar

- Revisados ocho textos y títulos con referencias físicas 105-108, incluido
  el carro del chwinga y el decreto bilingüe de Napaka.
- Conservadas las letras L/B/Z/V del mapa inglés de Wongo y las condiciones
  alternativas de maldición o combate. El enlace original de polimorfar
  contiene una etiqueta de cursiva dentro de su rótulo; requiere prueba visual.
- Conservadas las tiradas de presencia del Rey de Plumas: sus comentarios
  ingleses dicen «resultado de 1», aunque las fórmulas usan umbrales 50 y 25.
  Las capacidades insertadas de la ficha no quedan revisadas por este bloque.
- Corregida la bodega a un cuadrado de veinte pies de lado, frente a los
  veinte pies cuadrados del PDF. Conservada la detección probabilística de trampas.
- Auditorías técnica y editorial sin errores.

### ch3-papazotl-nangnang-01 a ch3-papazotl-nangnang-10 — Últimos santuarios orientales

- Revisados diez textos y títulos con referencias físicas 108-110, incluida
  la visión de Acererak junto a la cascada.
- El acertijo de Papazotl usa los seis versos españoles y la solución
  «tapar ojos». **Pendiente funcional:** adaptar y comprobar conjuntamente
  las ayudas 15 y 16 y su cuadrícula; revisar el texto no acredita que la
  cuadrícula original inglesa funcione con estos versos.
- Aclaradas la llegada de refuerzos grung y la apertura de Nangnang: solo
  una criatura dentro del santuario puede llevar sus falsos tesoros.
- La instrucción de activar Nangnang carece de enlace en el exportado.
- Auditorías técnica y editorial sin errores.

### ch3-obolaka-palace-01 a ch3-obolaka-palace-10 — Obo’laka y palacio real

- Revisados diez textos y títulos con referencias físicas 110-111.
- Conservadas las salvaciones repetidas al sostener el cubo, los ocho soportes,
  la forma de reencender las antorchas y las tres trancas de la puerta secreta.
- La inscripción mantiene la pista literal de permanecer en la luz, sin añadir
  «de la razón», que podría desviar la solución del acertijo.
- Conservadas ambas entradas al Fano y sus guardias por entrada.
- Completados los textos de los dos diarios principales del capítulo 3:
  treinta páginas de moradores y 58 de localizaciones. Las ayudas, fichas,
  tablas y escenas enlazadas siguen teniendo una revisión independiente pendiente.
- Auditorías técnica y editorial sin errores.

### ch4-intrigue-01 a ch4-intrigue-09 — Intrigas y acceso al Fano

- Revisados nueve textos y títulos con referencias físicas 112-113 y 115.
- Corregido el resentimiento de Fenthaza: Ras Nsi conserva restos de humanidad;
  el pasaje no se refiere a que esté obsesionado con peligros de su condición.
- Conservados los plazos de interrogatorio y trabajo, las condiciones de
  liberación, la transformación ofrecida y las consecuencias del golpe.
- Auditorías técnica y editorial sin errores. Las tablas enlazadas no quedan
  revisadas por el texto que explica su uso.

### ch4-tables — Tareas, refuerzos y tipo de corrupto

- Revisadas tres tablas del compendio: diecisiete resultados y tres títulos,
  con referencias físicas 113-114. No suman páginas de diario.
- Conservadas las contraseñas, destinos y tiradas. En las tareas, el inglés
  indica frotar a los yuan-tis que se bañan; el PDF habla de fregar los baños.
  Se sigue el exportado. En los refuerzos se conserva que la abominación muere,
  mientras que el PDF solo la da por derrotada.
- Incidencia original: el resultado de tipo 1 de `toaCh4YuantiMali` enlaza a
  `toaYuantiMal2000`, igual que el de tipo 2. Se conserva y requiere corrección
  técnica contrastada con las fichas. El título se aclara como selección de tipo.
- Auditorías técnica y editorial sin errores.

### ch4-roster-01 a ch4-roster-03 — Registro del templo y páginas de tablas

- Revisado el registro completo con referencia física 114: efectivos,
  movimientos, refuerzos y reacciones al gong, conservando sus 53 enlaces.
- Normalizado guardaestirpes; los gules que permanecen en el trono no son
  «demonios». La hidra exige recibir comida cuando acude al bote.
- Revisados los títulos de las dos páginas que insertan las tablas ya revisadas.
  Sus parámetros `resultLabel` siguen en inglés dentro del comando original;
  quedan pendientes de localización técnica y comprobación visual.
- Completadas las doce páginas del diario introductorio del capítulo 4.
- Auditorías técnica y editorial sin errores.

### ch4-access-01 a ch4-access-07 — Accesos, reglas y primeras salas

- Revisados siete textos y títulos con referencias físicas 115, 117-118 y 125.
- Conservadas las contraseñas, el habla de Ukurlahmu y la inmunidad al estado
  envenenado frente al gas; no se confunde con inmunidad al daño de veneno.
- Se conserva CD 15 del exportado para abrir por la fuerza la armería,
  frente a CD 25 en el PDF. Requiere decisión técnica al validar esa puerta.
- Incidencia original: la huida del triceratops hacia «zona 1» enlaza con
  `Jc7USn1q9dUkjEdI` (Características del templo), no con el portón.
- Los fragmentos de enlaces `#teleporters` requieren verificación frente
  al encabezado traducido. Automatismos de teletransporte y gas no probados.
- Auditorías técnica y editorial sin errores.

### ch4-prisoners-01 a ch4-prisoners-04 — Sacerdotisas y cautivos

- Revisados cuatro textos y títulos con referencias físicas 118-120.
- Conservadas las reglas actuales del oráculo, sin añadir la locura del PDF,
  y la fiebre de bruma azul de Sev. Normalizado Tesela y mantenida Salysa.
- La lista original anuncia diez cautivos pero contiene nueve: se presenta
  como ejemplos sin inventar un décimo. Cerrada la llave del rótulo de cansancio
  de Kanush, ausente en el exportado, conservando el comando de referencia.
- «Slapped in chains» significa encadenar: no se añaden las bofetadas del PDF.
  Los cráneos también dejan de cantar cuando termina el combate.
- Pendientes de navegación: el vínculo a Sekelok remite a zona 12 aunque
  figura en la 11; el fragmento `#prisoners-of-the-yuan-ti` debe comprobarse
  con el encabezado español. Los perfiles enlazados no quedan acreditados.
- Auditorías técnica y editorial sin errores.

### ch4-ras-nsi-01 a ch4-ras-nsi-04 — Fano, harén y Ras Nsi

- Revisados cuatro textos y títulos con referencias físicas 120-122.
- Corregido «skeleton crew»: queda una guardia mínima durante los rituales,
  no una patrulla de esqueletos. El ritual conserva sus efectos actuales,
  sin añadir la locura indefinida del PDF.
- El harén contiene una docena, no docenas. Los candelabros valen 75 po cada
  uno; las amatistas de Ras Nsi, 100 po cada una. Diferenciadas sus monedas
  de platino y plata. Acererak usó a los habitantes para construir la tumba.
- Conservados el desgaste de los escudos, las condiciones de traición del
  doppelganger y los atributos adquiridos durante el ritual.
- Los fragmentos `#yuan-ti-rituals` y `#teleporters` siguen pendientes de
  validación de navegación; las capacidades insertadas mantienen su revisión aparte.
- Auditorías técnica y editorial sin errores.

### ch4-service-01 a ch4-service-05 — Almacén, venenos y baños

- Revisados cinco textos y títulos con referencias físicas 122-124.
- Conservadas las condiciones de inhalación del incienso y su excepción para
  los yuan-tis, la ceguera de la aguja, el envenenamiento incluso al superar
  la salvación contra la jeringa y los vapores que afectan sin respirar.
- La llave de Xopal es de latón, no de cobre. El almacén recibe suministros
  de la superficie, no necesariamente de todos los rincones del mundo.
- Recuperada la referencia a humanos y minotauros esclavizados por Acererak
  en el relato de Yahru; el PDF omite a los primeros.
- El fragmento `#chultan-names` conserva su destino original y queda pendiente
  de comprobación de navegación. Auditorías técnica y editorial sin errores.

### ch4-caverns-01 a ch4-caverns-05 — Cubiles y cavernas

- Revisados cinco textos y títulos con referencias físicas 124-125.
- Conservados la prueba en grupo, los tiempos de llegada de la hidra y el
  estado de los cautivos. Los túneles del río están sumergidos, no solo bajo tierra.
- Eliminada una llave de cierre sobrante tras «commoners» en el alojamiento.
  La referencia del limo verde corresponde al capítulo 5, según el exportado.
- Completados los textos de ambos diarios principales del capítulo 4:
  doce páginas introductorias y 25 de localizaciones. Las tres tablas de tareas,
  refuerzos y tipos están revisadas; fichas, objetos, escenas y navegación,
  incluidos los problemas anotados, mantienen su trabajo pendiente.
- Auditorías técnica y editorial sin errores.

### ch5-history-spirits-01 a ch5-history-spirits-03 — Historia y dioses

- Revisados tres textos y títulos con referencias físicas 126-127 y 130-131.
- Conservados los nueve poderes, las condiciones de invisibilidad de Moa,
  la pérdida de toda sintonía al salir Obo’laka y la duración del efecto de Wongo.
- Aclaradas la permanencia de los espíritus en la tumba y la imposibilidad
  de volver a ocupar al mismo anfitrión después de resistirlos o expulsarlos.
- Normalizado NM para Nangnang. Acererak creó muertos vivientes y gólems de
  carne, sin añadir la categoría «gólems muertos vivientes» del PDF.
- Las cartas del apéndice F y los objetos vinculados siguen pendientes de
  revisión coordinada. Auditorías técnica y editorial sin errores.

### ch5-exploration-01 — Explorar la tumba

- Revisada una página extensa con referencias físicas 127-130: reglas generales,
  moradores, llaves-esqueleto, tesoros y tabla de restricciones mágicas.
- Conservados los 64 enlaces, la distribución de llaves, las excepciones para
  Acererak y su amuleto y las referencias expresas a las reglas de 2014.
- Cerrado correctamente el rótulo de zona 65. Aclarado el umbral pasivo de
  Percepción. Los espíritus rondan la tumba, sin afirmar que la defiendan.
- El que escapó de los Nueve Infiernos antes de decapitar al rey fue Ch’gakare.
  Las restricciones de magia siguen aplicándose dentro de espacios extradimensionales.
- Auditorías técnica y editorial sin errores.

### ch5-conclusion-01 — Consecuencias y cierre de la aventura

- Revisada la conclusión con referencias físicas 190-191 y sus 43 enlaces.
- Conservados los destinos alternativos de Syndra, el plazo de resurrección,
  las excepciones a la destrucción de objetos y los pactos posteriores con Fenthaza.
- Conservada la elección de Artus de mantener el anillo y el regreso de
  Acererak junto a su filacteria. Las capacidades legendarias de los cuatro
  tesoros siguen sujetas a decisión del director, como indica el original.
- Completadas las cinco páginas del diario introductorio del capítulo 5.
  Esto no implica que estén revisados sus seis niveles de localizaciones.
- Auditorías técnica y editorial sin errores.

### ch5-level1-entrance-01 a ch5-level1-entrance-06 — Acceso a los salones putrefactos

- Revisados seis textos y títulos con referencias físicas 131-133.
- La pista «Uno se alza entre ellos» conserva la posición central de Unkh,
  frente a «Uno destaca entre ellos» del PDF. «Las llaves solo giran por dentro»
  mantiene la otra pista. La ayuda 17 debe actualizarse junto con estas frases.
- En la advertencia, el inglés llama entrada falsa a la zona 2 y galería a la 3.
  Corregidos los nombres conforme a las páginas enlazadas y al PDF, conservando
  números y UUID: zona 2, galería; zona 3, entrada falsa.
- Conservados los seis éxitos necesarios para taponar la trampa activa y su
  rearme tras diez asaltos. Añadido rótulo español a la referencia de terreno difícil.
- Auditorías técnica y editorial sin errores.

### ch5-level1-doors-01 a ch5-level1-doors-07 — Puertas y primeras trampas

- Revisados siete textos y títulos con referencias físicas 133-134.
- Conservadas las parejas rivales de los cubos, la cuenta atrás, el rearme
  y las diferencias entre el daño inicial y el estado envenenado del foso.
- El reloj no se puede mover ni dañar; no se ha sustituido por la prohibición
  de reiniciarlo que aparece en el PDF. El demonio ataca al meter la mano.
- Pendiente técnico del original: el enlace de «disipar magia» de la cara de
  diablo apunta al UUID de detectar magia. Conservado el destino y traducido
  el rótulo según la regla descrita; requiere corrección funcional posterior.
- Auditorías técnica y editorial sin errores.

### ch5-level1-warnings-01 a ch5-level1-warnings-06 — Escalinata y advertencias

- Revisados seis textos y títulos con referencias físicas 135 y 140.
- Contrastada «Right the gods» con el foso del gólem: se giran las estatuas
  a la derecha. «Orienta a los dioses a la derecha» conserva esa dirección,
  ausente del «Reorienta» del PDF. «Sacia» conserva la pista de beber la sopa.
- Las ayudas 18-20 siguen pendientes de armonización con estas advertencias.
- Conservadas las dos salvaciones distintas de la cascada: evitar caer y
  evitar el daño tras la caída. Auditorías técnica y editorial sin errores.

### ch5-level1-hazards-01 a ch5-level1-hazards-06 — Fuente y trampas interiores

- Revisados seis textos y títulos con referencias físicas 135-139.
- Conservadas la atracción de todo tipo de metal, la protección del cuero,
  el fallo por cinco del cofre y sus cinco asaltos de aire incluso fuera del agua.
- Diferenciados los daños de la hélice según su velocidad y el atasco corporal.
- Añadidos rótulos españoles a Asfixia y al estado apresado.
- La atracción mágica repite el enlace incorrecto del original de «disipar
  magia» a detectar magia. Pendiente técnico, igual que la cara de diablo.
- La tabla insertada de efectos de la fuente queda pendiente de revisión propia.
- Auditorías técnica y editorial sin errores.

### ch5-level1-tombs-01 a ch5-level1-tombs-03 — Tumbas de los embaucadores

- Revisados tres textos y títulos con referencias físicas 136-140.
- Conservados el alcance y las limitaciones del disco de ojos y la diferencia
  entre abrir el sarcófago con máscara y sin ella. Corregido el rótulo partido
  del espíritu de Obo’laka sin cambiar las etiquetas HTML.
- Conservados los tres fallos de Engaño de Nepartak y la llegada de los
  enjambres al comienzo del asalto siguiente, no al instante.
- Aclarado que los botones desbloquean los cofres y activan sus trampas
  simultáneamente; el de hierro afecta a cualquier metal no mágico.
- Completadas las 28 páginas de texto del diario del nivel 1. Sus actores,
  objetos, cartas y tabla insertada conservan sus revisiones independientes pendientes.
- Auditorías técnica y editorial sin errores.

### ch5-level2-access-01 a ch5-level2-access-05 — Accesos y vigilancia

- Revisados cinco textos y títulos con referencias físicas 140, 142-143 y 145.
- Conservados el mecanismo de los tres zombis, el alcance de la observación
  a través del guardián y la excepción del amuleto llevado por un observador.
- Corregida la unión entre texto y enlace del nivel 2 en la escalera.
- El foso del diablo repite el UUID incorrecto de disipar magia a detectar magia.
  Queda anotado para la revisión técnica de enlaces.
- Auditorías técnica y editorial sin errores.

### ch5-level2-mirror-01 a ch5-level2-mirror-02 — Anillo y tumba falsa

- Revisados dos textos extensos y títulos con referencias físicas 140-142.
- Conservados el reinicio diario del semiplano, la captura por el Almero y
  la diferencia entre quitar la maldición al portador y eliminarla del bastón.
- Aclaradas las manos y los pies con dos dedos del original y la inundación:
  respirar agua no permite respirar vino; los extraños llegan en el tercer asalto.
- Corregido el rótulo partido del perfil del extraño de agua y añadido el
  de invisible. El grimorio insertado sigue pendiente de su propia revisión.
- Pendiente técnico del original: detectar magia en el ataúd enlaza al UUID
  de disipar magia, inverso a los errores de enlaces anotados anteriormente.
- Auditorías técnica y editorial sin errores.

### ch5-level2-tombs-01 a ch5-level2-tombs-02 — Papazotl y Nangnang

- Revisados dos textos y títulos con referencias físicas 143-144.
- El aura de las marmitas es de conjuración según el inglés, no de abjuración
  como en el PDF. Conservados los refuerzos por marmita y la excepción del escudo
  para quienes se inclinen ante la estatua sin rostro.
- Corregidos los errores del PDF «CA 18» y «amuleto» por CD 18 y huevo.
  Mente en blanco evita música y daño psíquico, sin añadir una exención del baile.
- Conservado el precio individual de cada broche de oro y aclarado que el slaad
  queda libre al entrar en el círculo, además de al atacarlo o alterar la sal.
- Auditorías técnica y editorial sin errores.

### ch5-level2-residents-01 a ch5-level2-residents-03 — Genio, Mustio y fragua

- Revisados tres textos y títulos con referencias físicas 143-147.
- Conservados los tratos de Keshma y su fracaso al salir mediante magia planar.
- Usado Gorra del export y mantenidas Khomara/Blackfire como palabras de mando;
  deben coincidir con el espejo y sus objetos. El PDF traduce Blackfire como
  Fuego Negro. El pájaro cantor no se restringe a una especie no indicada en inglés.
- La fragua conserva el juego adicional de herramientas de artesano del export.
  Se describe al gólem como animado, evitando convertir el «undead» narrativo
  del original en una clasificación de criatura incompatible con su perfil.
- Pendiente técnico: el comentario de la tirada porcentual dice «result of 1»
  aunque comprueba 50 %. Conservados fórmula y comentario, como en casos previos.
- Completadas las doce páginas de texto del nivel 2. La ficha de Mustio y su
  Lanzamiento de Conjuros insertado quedan pendientes de revisión propia.
- Auditorías técnica y editorial sin errores.

### ch5-level3-halls-01 a ch5-level3-halls-07 — Primeros pasillos del nivel 3

- Revisados siete textos y títulos con referencias físicas 147-148.
- Conservados el orden invertido de las figuras y armas de los dos pasillos,
  las posiciones de los ojos y el efecto de la cortina incluso al superar la salvación.
- Aclarado que la máscara muestra el pasado y se reinicia al apartar todos la vista.
- Cerrado correctamente el rótulo de zona 31A, que incluía el paréntesis del
  texto exterior. El moho solo responde con un rayo al destruir una mancha,
  según el export, no ante cualquier daño como sugiere el PDF.
- Auditorías técnica y editorial sin errores.

### ch5-level3-puzzles-01 a ch5-level3-puzzles-05 — Túneles, sombra y jeroglíficos

- Revisados cinco textos y títulos con referencias físicas 148-151.
- Conservados los sentidos de giro, descenso y ascenso de los túneles y
  el reparto del aire según el número de ocupantes. Traducida la limitación
  original de los muros norte-sur de la escena; pendiente de validación en juego.
- El duplicado debe beber la sopa para revelar el tesoro; disiparla no basta.
  Conservada la excepción de inmunidad al miedo ante su rostro.
- Revisada la secuencia buitre-serpiente-puerta-junco-escarabajo-cetro-pie-urna,
  la mirilla telepática y la diferencia entre retirar el medallón y retirar el disco.
- Corregidos rótulos con paréntesis mal colocados en dos enlaces de zona 44.
- Auditorías técnica y editorial sin errores.

### ch5-level3-ijin-01 a ch5-level3-ijin-02 — Interior de I’jin y descanso

- Revisados dos textos y títulos con referencias físicas 151-152.
- La secuencia coincide con el disco de acceso y no se reinicia al fallar.
  Conservadas la CD 7 del bloque y la llegada posterior de los reparadores.
- La nube de langostas afecta a la primera entrada en cualquier turno,
  no solo en el propio, conforme al original inglés.
- Conservadas las condiciones exclusivas para abrir el sarcófago, el campo
  de fuerza y los valores y colores de los tesoros.
- Auditorías técnica y editorial sin errores.

### ch5-level3-mechanisms-01 a ch5-level3-mechanisms-05 — Viento y sala giratoria

- Revisados cinco textos y títulos con referencias físicas 152-153.
- Los vientos usan el daño psíquico del export actualizado. No se han añadido
  la locura temporal ni las inmunidades de autómatas y muertos vivientes del PDF.
- Conservada la transparencia en un solo sentido de la sala de control,
  las excepciones al daño por giro y los tres conjuros de abrir necesarios.
- La tabla insertada de efectos del tambor requiere su propia revisión.
- Auditorías técnica y editorial sin errores.

### ch5-level3-guardians-01 a ch5-level3-guardians-03 — Gólem, Yaka y guardianes

- Revisados tres textos y títulos con referencias físicas 154-155.
- Conservado el giro a la derecha de ambas estatuas, coherente con la advertencia,
  y la protección del metal encerrado en recipientes sellados frente al gas.
- Yaka es un bufón, no simplemente un necio; su silencio mágico evita la
  desventaja sin levantar por ello la maldición.
- Pendiente de contenido enlazado: el texto exportado de los guardianes omite
  el apartado del PDF sobre la cadena de pinchos (distancia, daño compartido,
  resistencia y rotura). Revisar su ficha antes de decidir si falta en el módulo.
- Conservada «Selected» como rótulo de interfaz del original hasta comprobar
  la versión de Foundry empleada. Auditorías técnica y editorial sin errores.

### ch5-level3-kubazan-01 — Ritual de Kubazan

- Revisado texto completo y título con referencias físicas 155-156.
- Conservadas las cuatro acciones en cualquier orden y la máscara obligatoria
  en cada una. Diferenciadas la trampa por ritual incorrecto y la rociada por
  abrir el sarcófago sin ritual; esta afecta también al pasillo sur.
- Conservadas las flechas de un punto de daño y la posesión al tocar cualquiera
  de los brazales. El enlace junto a los huesos del ranamot lleva a la
  introducción del apéndice D, un destino genérico válido.
- Auditorías técnica y editorial sin errores.

### ch5-level3-beholder-01 a ch5-level3-beholder-04 — Velos y Belchorzh

- Revisados cuatro textos y títulos con referencias físicas 156-158.
- Diferenciados miedo del tapiz y hechizo del jabalí: distintas salvaciones,
  condiciones de repetición y duraciones de inmunidad tras superarlas.
- Las cavidades de los ojos tienen una pulgada de diámetro, no de profundidad
  como indica el PDF. Conservadas todas las ubicaciones de las diez llaves.
- Conservados el aura de Nystul de 2014, la adhesión a la esfera, la diferencia
  entre cubrirla y disiparla y la represalia mediante moho por robar tesoro.
- El fragmento original `#alien-growth` requiere validación de navegación tras
  traducir su encabezado, como los fragmentos ya anotados en otros capítulos.
- Completadas las 27 páginas de texto del nivel 3. Auditorías sin errores.

### ch5-level4-access-01 a ch5-level4-access-04 — Acceso a las Cámaras del Horror

- Revisados cuatro textos y títulos con referencias físicas 158-159.
- Conservados los diezmos por humanoide y pedestal, el pago equivalente y la
  distinción entre plata (pp) y platino (ppt). El tesoro oeste conserva cobre
  del export, frente a la errata de electro del PDF.
- Conservado el idioma druídico del lagarto y el campo antimágico de las celdas.
- El enlace de las gárgolas al apéndice D lleva a su introducción; es válido.
- Auditorías técnica y editorial sin errores.

### ch5-level4-cells-01 a ch5-level4-cells-04 — Celdas elementales

- Revisados cuatro textos y títulos con referencias físicas 159-161.
- Corregida una errata decisiva del PDF: en el cuarto asalto el agua apaga
  la vela; no se detiene la inundación. Arrancar el primer molusco disipa el
  campo antimágico, y comerlo determina el destino del teletransporte.
- Conservadas la precaución de aguantar la respiración antes de llegar al aire
  y la disipación al extraer el primer hueso, previa a inhalar su contenido.
- En tierra, la Destreza es una salvación, no una prueba de característica.
  Conservados el umbral de arena, los rodillos y el bloqueo del botón de salida.
- Auditorías técnica y editorial sin errores.

### ch5-level4-shagambi-01 — Tumba de Shagambi

- Revisado texto completo y título con referencias físicas 161-162.
- Diferenciadas llegada a una runa y entrada desde fuera: la norte daña al llegar;
  la sur transforma al usarla para salir. Conservadas las cuatro formas animales.
- Conservados el único aviso de los guerreros, su destrucción por crítico y
  la caja de música que los activa incluso sin ruidos previos.
- Mantenida la referencia a la mandolina de las reglas de 2014. Pendiente
  técnico: fragmento `#terracotta-warriors`. El enlace de kamadan al apéndice D
  lleva a su introducción; es válido.
- Auditorías técnica y editorial sin errores.

### ch5-level4-maze-01 a ch5-level4-maze-04 — Laberinto de la muerte

- Revisados cuatro textos y títulos con referencias físicas 162-164.
- Diferenciados los gestos de entrada y salida, el brazo derecho amputado
  y la imposibilidad de mover o controlar la esfera de aniquilación.
- Conservados los dos efectos simultáneos al retirar la corona y el valor
  multiplicado en subasta. El fragmento `#fabled-treasures` requiere revisión
  técnica. El enlace de bodak lleva a la introducción del apéndice D; es válido.
- Auditorías técnica y editorial sin errores.

### ch5-level4-mirror-01 — Espejo atrapavidas

- Revisado texto, tabla de doce celdas y título con referencia física 164.
- Conservadas las tres celdas vacías, la liberación aleatoria al llenarse y
  las reacciones simultáneas al destruir el espejo.
- Khomara y Blackfire coinciden con el grimorio descrito en la oficina de Mustio.
  Corregido NM para Tlad y aclarado que Zaal obedece a Lukanu.
- Los enlaces de gárgola y campeona llevan a la introducción del apéndice D;
  son válidos. Auditorías técnica y editorial sin errores.

### ch5-level4-royal-01 a ch5-level4-royal-03 — Puerta, trono y Reina del Sol

- Revisados tres textos y títulos con referencias físicas 165-167.
- Los artistas están cubriendo las pinturas de la Compañía del Estandarte Amarillo,
  no creándolas, como parecía en el PDF. Conservadas sus limitaciones y la
  aparición del tiranosaurio al expulsar o destruir a cualquiera de ellos.
- Napaka es la anciana reina, sin añadir el título de reina madre del PDF.
- Diferenciados calor y rayos del sol, collar maldito y gas del sarcófago;
  el intercambio inmediato del cetro evita solo el desencadenante correspondiente.
- Conservados sus conocimientos sobre Zalkoré y su desconocimiento del destino
  de sus bisnietos. Auditorías técnica y editorial sin errores.

### ch5-level4-clock-01 a ch5-level4-clock-05 — Bola, ácido y reloj

- Revisados cinco textos y títulos con referencias físicas 167 y 169.
- Separados los desencadenantes del cofre, la bola y la tapa del foso.
  El ácido causa daño al entrar por primera vez en cualquier turno.
- La llave es de latón; su invisibilidad puede disiparse, mientras que la
  puerta invisible del reloj no admite disipación. Conservado el límite
  de 24 horas para revertir el envejecimiento.
- Unificado Ombligo de la Luna con las referencias narrativas anteriores.
- Auditorías técnica y editorial sin errores.

### ch5-level4-unkh-01 a ch5-level4-unkh-02 — Unkh y pozo del olvido

- Revisados dos textos y títulos con referencias físicas 167-169.
  Completados los 24 textos del cuarto nivel.
- El don corresponde a quien recuperó la llave, no necesariamente a quien
  la introduzca. La eliminación de la marca no se presenta como eliminación del don.
- Conservadas separación, visibilidad y expulsión del laberinto. La tabla
  insertada y los objetos de encantamiento siguen pendientes de revisión propia.
- El original del módulo omite la inversión de las funciones de las palancas
  al regresar al pozo, presente en el PDF. No se ha añadido una regla que la
  macro podría no implementar: requiere contrastar texto y automatización.
- Auditorías técnica y editorial sin errores.

### ch5-level5-gears-01 a ch5-level5-gears-05 — Engranajes del odio

- Revisados cinco textos y títulos con referencias físicas 170-171 y 175.
- El légamo daña en el primer contacto de cualquier turno, no solo el propio.
  Los techos y el conducto no giran con las cámaras.
- Los armarios solo pueden abrirse sucesivamente; el rastrillo exige matar
  a sus criaturas en esta sala. Conservados el reinicio y las limitaciones
  de los portales de sentido único.
- El original describe luces visibles al abrir Shadowfell y, a continuación,
  fuegos fatuos invisibles hasta atacar. Se conserva esa discrepancia narrativa
  para decidir su presentación durante la comprobación de la escena.
- Auditorías técnica y editorial sin errores.

### ch5-level5-controls-01 — Sala de control

- Revisado texto y título con referencias físicas 171-173.
- Corregida la configuración 1 conforme al original: 58 conecta con 60 y 63;
  59 queda aislada. El PDF incluye 59 también entre las conexiones.
- Diferenciados selector y botón de giro, palanca de vertido, cierre de la
  salida y enlace telepático. Se mantienen las restricciones para taponar
  tuberías y liberar a una criatura atrapada bajo la pared.
- Conservado Gorra, nombre original de Mustio, y los 36 destinos UUID.
- Auditorías técnica y editorial sin errores.

### ch5-level5-napaka-01 a ch5-level5-napaka-06 — Mole de piedra y gas

- Revisados seis textos y títulos con referencias físicas 173-174.
- Diferenciados los desencadenantes de la mole y la inmunidad de la estatua
  frente a la vulnerabilidad de su brazo roto. Conservados los nueve sacrificios
  de gemas y el efecto del cetro con y sin tirada de ataque.
- La orden «¡Despertad a Napaka!» se dirige a los exploradores; su ayuda gráfica
  insertada deberá armonizarse al revisar las imágenes.
- El gas afecta aunque no se respire, pero no a plantas. Corregida la frase
  inglesa confusa del conducto: está en el techo de 58 y el gas no asciende por él.
- Retirada una comilla sobrante tras Tesoros legendarios. El enlace de la mole
  lleva a la introducción del apéndice D; es válido.
- Auditorías técnica y editorial sin errores.

### ch5-level5-lake-01 a ch5-level5-lake-02 — Lago y puerta de la voracidad

- Revisados dos textos y títulos con referencias físicas 175-176.
- El aboleth ignora los botes independientemente de su personalidad, no de
  cualquier conducta del grupo; carece de acciones en guarida.
- Adaptada la pista inglesa «light» como «que brille»: «ligero» en el PDF
  pierde la referencia a la fosforescencia necesaria para resolver la puerta.
- Diferenciadas la apertura desde cada lado, la supresión temporal de la boca
  y la deglución automática. La jaula permite respirar y ofrece cobertura.
- La linterna del Depredador es de ojo de buey según el original y el objeto
  enlazado, no sorda como figura en el PDF.
- Auditorías técnica y editorial sin errores.

### ch5-level5-mastodon-01 — Salón del mastodonte dorado

- Revisado texto y título con referencias físicas 176-177.
- Restituido el diablo barbado entre las figuras de los murales, omitido en
  el PDF. Conservada la secuencia de encuentros de los asaltos 2 a 6.
- Diferenciados aplastamiento letal, fuego del suelo y posiciones seguras
  sobre Ghom. El sacrificio pactado conserva el destino del alma y del equipo.
- El viento trae polvo de sepultura, no polvo rocoso. Ch’gakare se recompone
  si lo destruyen; la salida se abre cuando desaparece.
- Auditorías técnica y editorial sin errores.

### ch5-level5-final-01 a ch5-level5-final-03 — Podredumbre, cadena y esfera

- Revisados tres textos y títulos con referencias físicas 177-179.
  Completados los 18 textos del quinto nivel.
- La podredumbre solo afecta a los materiales y objetos no mágicos indicados;
  reparar no los restaura. Retirar la argolla termina el efecto.
- Aclarado que el salto con pértiga es del balcón oriental al occidental,
  más elevado. Conservados el vehículo del pentadron y sus limitaciones.
- Conservadas las excepciones de decapitación y la avería tras la conjunción.
  El original no precisa la frecuencia del daño de sobrecarga de la esfera;
  no se ha inventado una cadencia por turno. La tabla insertada sigue pendiente.
- Auditorías técnica y editorial sin errores.

### Ajuste terminológico — Dones de Unkh

- Recontrastadas las referencias físicas 168-169: los dones se denominan
  sortilegios y el objeto es la túnica de colores hipnóticos.
- Adoptados los nombres del PDF: sentir tesoros, saga tumefacta, mutilados
  y gules. Se han actualizado los registros existentes, sin sumar páginas.
- Esta nomenclatura deberá trasladarse a las fichas de los objetos pendientes.
- Auditorías técnica y editorial sin errores.

### ch5-level6-sisters-01 a ch5-level6-sisters-02 — Hermanas Cosidas

- Revisados dos textos y títulos con referencias físicas 179-182.
- Adoptados Briznas, Clay Sinrostro, Joho, Calderilla, Peggy Ánimas,
  Ancha Yaya y Don Remiendos conforme al PDF. Sus fichas siguen pendientes.
- Conservados límites y requisitos de los sortilegios, conocimientos actuales
  del clon y destino de las almas si se destruyen los muñecos.
- Las sagas atacan al quedar expuestas las cinco cerraduras si el grupo tiene
  las llaves, no después de abrir la puerta. Diferenciadas las dos operaciones.
- El enlace de «Activar la escena» apunta a un diario en el original;
  se conserva y queda pendiente de corrección en la revisión funcional.
- Auditorías técnica y editorial sin errores.

### ch5-level6-trials1-01 a ch5-level6-trials1-03 — Primeras pruebas

- Revisados tres textos y títulos con referencias físicas 182-184.
- Conservadas las alternativas mágicas y geométricas del cilindro y la palanca.
- Torbellino daña a todas las criaturas empatadas con el resultado más bajo,
  conforme al original plural. Las órdenes Bicharraco, Escupitajo y Torbellino
  deberán coincidir con las actividades del mephit al revisar sus fichas.
- Diferenciados beneficios, perjuicios ocultos y automatización del banquete.
  La maldición por hambre afecta a quien sale sin haber comido ni bebido.
- Sustituida la etiqueta errónea «Revert Transformoration» por una descripción
  de la opción. Su ubicación y «Illusory» requieren comprobación de interfaz.
- Auditorías técnica y editorial sin errores.

### ch5-level6-trials2-01 a ch5-level6-trials2-02 — Últimas pruebas

- Revisados dos textos y títulos con referencias físicas 184-185.
- El espejo permite accionar solo la palanca que se ve reflejada. Conservadas
  la sexta vela oculta, la palanca falsa y la única convocatoria de hombres jabalí.
- Adaptada la cancioncilla a ocho versos rimados, manteniendo los dos órdenes
  de lectura y sus consecuencias.
- Corregido el PDF: abrir el compartimento por el procedimiento de la canción
  inversa no activa la trampa. Sí lo hacen las herramientas o el conjuro abrir.
- Conservados el falso foso, la altura real, el daño recurrente y el único uso.
- Auditorías técnica y editorial sin errores.

### ch5-level6-nursery-01 — Almero, atropal y Acererak

- Revisado texto y título con referencias físicas 185-187.
- Separadas la liberación de almas al destruir el Almero y la llegada de
  Acererak al morir el atropal. La rotura de un puntal derriba los otros dos.
- Conservados respuesta de tentáculos por turno, límites de peso y alcance,
  caídas, vulnerabilidades y beneficios mientras se ve a Acererak.
- La huida ocurre en el siguiente turno al bajar de 100 PG; destruir el cuerpo
  no destruye la filacteria remota. La esfera no atraviesa el portal por sí sola.
- El comentario del dado de filacterias dice «resultado 1» aunque el umbral
  implementa el 10 % correcto. Se conserva el comando; pendiente de ajuste técnico.
- Los enlaces del atropal y Acererak llevan a la introducción del apéndice D;
  son válidos. El otro enlace de introducción y el fragmento `#mist-gate`
  requieren revisión.
- Auditorías técnica y editorial sin errores.

### ch5-level6-passages-01 a ch5-level6-passages-02 — Capilla y sendas

- Revisados dos textos y títulos con referencias físicas 187-189.
- Conservadas identidad opcional del prisionero, agua bendita como solución
  y respuesta de los nóticos. Su pista dirige la atención a los huesos.
- El muro de fuego ocupa anchura y altura, no toda la longitud del pasillo
  como indica el PDF. Se mueve hacia el norte tras activar o disipar el glifo.
- Diferenciados colgante protector, senda morada temporal y senda roja.
  La automatización de esta última teletransporta al cruzar la pared: debe
  comprobarse cómo aplicar el requisito narrativo de recorrer la senda.
- Auditorías técnica y editorial sin errores.

### ch5-level6-exit-01 a ch5-level6-exit-02 — Biblioteca y salida

- Revisados dos textos y títulos con referencias físicas 189-190.
  Completados los 12 textos del sexto nivel y los 126 del capítulo 5.
- El nombre verdadero aturde al arcanaloth; tras el efecto hay 24 horas de
  inmunidad a su repetición. Las gafas son la llave de un portal, no mágicas.
- Corregida la descripción de «gafas de oro» en el consejo de Foundry para
  mantener concordancia con las gafas de carey descritas; las fichas deben revisarse.
- Diferenciados objetos sueltos perdidos en el cieno y equipo que acompaña
  a las criaturas al salir. Conservadas duración y reactivación por canica.
- Auditorías técnica y editorial sin errores.

### ch5-tables — Cuatro tablas del capítulo 5

- Revisados nombres y resultados de fuente mágica, sala giratoria, laberinto
  y esfera armilar: 30 campos del compendio de tablas, sin sumar páginas de diario.
- Referencias físicas 136, 154, 168 y 179. Conservados intervalos, tiradas,
  enlaces y condiciones de recuperación, daño y transformación.
- La curación de la esfera excluye a quienes estén dentro del globo; el aumento
  de Inteligencia sigue siendo permanente y limitado a 22.
- Esta revisión acredita el compendio de tablas; las copias internas del
  Adventure, si existen, deben contrastarse al revisar los documentos incorporados.
- Auditorías técnica y editorial sin errores.

### appendix-ac-journals-01 a appendix-ac-journals-21 — Apéndices A y C

- Revisados 21 textos y títulos: tres del apéndice A y dieciocho del C,
  con referencias físicas 192-193 y 206-209.
- Revisadas introducciones, tabla de precios de flora y fauna, categorías
  y etiquetas de inserción. No se acredita todavía el contenido de los objetos
  o trasfondos insertados ni las tres páginas de imágenes del apéndice C.
- Conservada Linterna fantasma por coherencia con los textos ya revisados;
  el PDF emplea Linterna fantasmal. Se armonizarán las fichas con la decisión final.
- El Bastón del Olvidado figura como artefacto en el original del módulo;
  se conserva frente a «legendario» en el PDF, pendiente de contrastar su ficha.
- Retirada la letra sobrante al final de la introducción de trasfondos.
  El `@Embed` del antropólogo conserva la comilla sobrante de `caption=false"`;
  requiere corrección técnica y prueba de inserción.
- Comprobado que `Adventure.tables` está vacío: no hay copias internas de las
  tablas que sincronizar en este exportado.
- Auditorías técnica y editorial sin errores.

### appendix-c-flora-01 a appendix-c-flora-08 — Fichas de flora y fauna

- Revisados los 34 campos textuales de ocho objetos: descripciones, nombres,
  actividades y efectos, contra la referencia física 206 y el exportado inglés.
- Conservados dosis, caducidad, repetición de salvaciones y límites de uso.
  La nota de sinda explica que las bayas se contabilizan mediante usos máximos.
- Verificada la actividad de ryath: el comando contextual `[[/heal]]` usa
  2d4 PG temporales. Su falta de cifra explícita no implica una curación ordinaria.
- Yahcha trata fiebre de la bruma azul en el original actualizado; se mantiene
  frente a fiebre del mono loco en el PDF, como en el capítulo 2 revisado.
- `Adventure.items` está vacío: no contiene copias directas de estos objetos.
  Los objetos dentro de actores o deltas de fichas requieren revisión separada.
- Auditorías técnica y editorial sin errores.

### appendix-c-magic — Amuleto, Marcapáginas y máscara

- Revisados 12 campos de tres objetos y siete de la tabla de transformaciones
  del Cráneo Negro, con referencias físicas 207 y 209.
- Conservada la excepción de teletransporte del amuleto y el efecto sobre
  portadores no muertos vivientes. La tabla mantiene sus seis resultados.
- Corregido el alcance de compulsión de Marcapáginas: aumenta a 90 pies,
  no en 90 pies como dice el PDF. Solo afecta a arañas de tipo bestia.
- Revisados también nombres de actividades y efectos de la daga.
- Auditorías técnica y editorial sin errores.

### appendix-c-magic — Linterna y armadura del escorpión

- Revisados diez campos de dos objetos con referencias físicas 208-209.
- La linterna estabiliza a su portador inconsciente dentro del alcance;
  liberar el espíritu elimina la magia del objeto. No puede dañarse ni expulsarse.
- La armadura elimina sus propias desventajas, sin conceder una ventaja general.
  Conservadas la condición del bonificador de iniciativa y la maldición al
  ponerse o quitarse la armadura. Su bloque secreto mantiene la visibilidad.
- Auditorías técnica y editorial sin errores.

### appendix-c-magic-staff — Bastón del Olvidado

- Revisados doce campos con referencias físicas 208-209, incluidos efectos y
  actividades. Conservada la sección secreta y la sintonización por clase.
- Contrastadas las actividades contextuales: maldición con Constitución y CD
  de conjuro; posesión con Carisma CD 20; destrucción con Destreza CD 18 y
  24d10 de fuerza, mitad al salvar.
- Restituido el tipo necrótico del daño adicional, omitido en el PDF.
- El efecto del original contiene `&Reference[blinded, &Reference[charmed ...]`
  sin cerrar la primera referencia; se conserva como incidencia técnica pendiente.
- La ficha exige sintonización pero no aporta rareza en `system.rarity`;
  sigue pendiente resolver la categoría discrepante del encabezado del diario.
- Auditorías técnica y editorial sin errores.

### appendix-c-magic-ring — Anillo del Invierno

- Revisados 21 campos con referencias físicas 207-208: descripción, texto
  de chat, actividades y efectos. Completadas las siete fichas principales
  de objetos mágicos del apéndice C; sus copias y conjuros propios siguen pendientes.
- Conservados consciencia, control, restricciones de adivinación y diferencia
  entre envejecimiento natural y mágico. No se añaden inmunidades generales.
- Las temperaturas conservan las cifras originales y explicitan Fahrenheit,
  también en el chat. No se mezclan con las aproximaciones Celsius del PDF.
- Conservadas cargas, variantes de conjuros, creación de objetos y autómatas,
  duración, derretimiento y destrucción por la Reina del Verano.
- Auditorías técnica y editorial sin errores.

### appendix-a-anthropologist — Antropólogo y tablas

- Revisados 42 campos: trasfondo, rasgo Lingüista experto y cinco tablas,
  con referencia física 192.
- Conservados equipo, competencias y observación durante un día antes de
  comunicarse de forma rudimentaria. No se concede dominio pleno de un idioma.
- Revisados cultura adoptada, personalidad, ideales, vínculos y defectos;
  conservados resultados e indicaciones de alineamiento del original.
- Auditorías técnica y editorial sin errores.

### appendix-a-archaeologist — Arqueólogo y tablas

- Revisados 43 campos: trasfondo, Conocimiento histórico y cinco tablas,
  con referencia física 193. Cerrados ambos trasfondos principales y sus tablas.
- Corregidos caudillos frente a brujos y aventuras arqueológicas frente a
  explotación arqueológica. Conservadas competencias, equipo y elección de objeto.
- El rasgo determina el propósito original y los constructores de ruinas,
  y el valor de objetos de arte de más de un siglo; no añade una prueba.
- Auditorías técnica y editorial sin errores.

### appendix-f-trickster-cards — Tarjetas de los dioses embaucadores

- Revisados los nueve documentos insertados y sus nueve páginas de diario:
  51 registros, con referencia física 257. Incluye actividades y efectos.
- Adaptadas las pronunciaciones al español y mantenidas las especies y el
  género de los dioses. «Self-absorbed» se expresa como «absorta en sí misma».
- Conservadas las condiciones de invisibilidad, las tres puntuaciones de 23,
  la pérdida de todas las sintonías de Obo'laka, las pruebas de Sabiduría de
  Papazotl y los límites del ataque adicional y del asalto psiónico.
- Auditorías técnica y editorial sin errores; pendiente comprobar las tarjetas
  y los efectos en Foundry junto con el resto del módulo.

### appendix-b-start — Uso de encuentros y primeras criaturas

- Revisadas ocho páginas (16 registros): introducción, Puerto Nyanzaru,
  naturaleza, aarakocras, enanos albinos, aldanis, almirajes y simios.
- Referencias físicas 194, 197, 200 y 204. Conservados frecuencia, umbrales,
  condiciones de sorpresa, soborno de los aldanis y apaciguamiento del almiraj.
- Los UUID genéricos de chwingas, enanos, aldanis y almirajes llevan a la
  introducción del apéndice D; son válidos. La etiqueta `Encounter` del Embed
  requiere comprobar la traducción de parámetros de presentación.
- Auditorías técnica y editorial sin errores.

### appendix-b-artus — Artus, depredadores y encuentros sociales

- Revisadas nueve páginas (18 registros): Artus Cimber, enredaderas asesinas,
  picos de hacha, babuinos, alijo, caníbales, chwinga, cocodrilos y cíclope.
- Referencias físicas 197, 198, 201 y 203. Conservadas las alternativas al
  combate, la comida diaria por cada babuino y las variantes diurna y nocturna.
- El cocodrilo realiza la prueba para volcar la canoa; el cíclope tira dos
  veces para obtener tesoro. Las enredaderas no se descubren por Percepción.
- Auditorías técnica y editorial sin errores.

### appendix-b-dinosaurs — Encuentros con dinosaurios

- Revisadas catorce páginas (28 registros), con referencias físicas 198–200.
- Conservadas cantidades, distancias, precios, defensa de las crías y las
  condiciones para evitar el combate. Frente a los plesiosaurios basta alcanzar
  un lugar seguro en la orilla; el PDF añade «otra orilla» sin apoyo del inglés.
- Tiranosaurio: se mantiene el inglés exportado con pruebas individuales y
  ventaja si alguien tiene Supervivencia. El PDF dice prueba de grupo: queda
  registrada la diferencia para la comprobación de reglas. La fórmula del
  50 % es correcta, pero su comentario técnico inglés dice «result of 1»;
  se suma a los comentarios de tirada pendientes de corrección funcional.
- Auditorías técnica y editorial sin errores.

### appendix-b-factions — Dragones, facciones y exploradores

- Revisadas nueve páginas (18 registros): dragones feérico y rojo, eblis,
  Enclave Esmeralda, explorador muerto, exploradores, salamandras flamígeras,
  caracol flagelo y Puño Ardiente. Referencias físicas 198, 200, 201, 203 y 204.
- Corregidos el secuestro de los eblis («llevarse a rastras») y la plataforma
  del Enclave (cuadrado de 10 pies de lado, no 10 pies cuadrados).
- Conservadas las patrullas, los permisos y los golpes para dejar inconsciente.
  El Enclave conserva la prueba exportada; el PDF añade que es de grupo.
- Yesca sigue siendo joven en este encuentro, como dicen ambos textos de
  referencia; la biografía insertada del actor pendiente la llama adulta.
  Hay que resolver esa discordancia al revisar el actor y su adaptación.
- Auditorías técnica y editorial sin errores.

### appendix-b-giants — Animales voladores y criaturas gigantes

- Revisadas once páginas (22 registros), con referencias físicas 197, 198,
  201–204: monos y serpientes voladores, gigantes de escarcha, jabalíes,
  cocodrilo, ranas, lagartos, escorpiones, tortuga, avispas y girallons.
- Conservados adiestramiento semanal, captura, precios, pruebas de grupo y
  contagio al final del encuentro para quienes hayan sufrido daño.
- Pendientes funcionales del original: la tirada de los girallons usa `dex`
  aunque la etiqueta exige Sigilo; el comentario de Drufi dice resultado 1
  aunque la fórmula implementa correctamente la probabilidad del 20 %.
- Auditorías técnica y editorial sin errores.

### appendix-b-ambushes — Emboscadas y encuentros mágicos

- Revisadas doce páginas (24 registros), con referencias físicas 197 y 201–204:
  goblins, grungs, jaculis, kamadans, hombres lagarto, bruma mágica, magmins,
  atrapahombres, mephits, saga de la noche, hombres pterodáctilo y plantas raras.
- Conservados avisos nocturnos con desventaja, recompensas y condiciones de
  retirada. La bruma usa la fiebre de la bruma azul del módulo actualizado.
- Añadido el comentario de probabilidad de crías de kamadan a los pendientes:
  fórmula del 25 % correcta, comentario inglés «result of 1» incorrecto.
  La etiqueta interna `Plant Type` del Embed queda para comprobar presentación.
- Auditorías técnica y editorial sin errores. La página de plantas raras
  contiene un Embed; su tabla se revisará como documento independiente.

### appendix-b-swamps — Serpientes, sagas y enjambres

- Revisadas catorce páginas (28 registros), con referencias físicas 197,
  200–204: Mago Rojo, salamandra, sagas de los mares, broza movediza,
  tres serpientes, arañas, estatua de Ubtao, estirges, sucarates y tres enjambres.
- Conservados rendición del Mago Rojo, sorpresa, tres tiradas de tesoro de las
  sagas y la condición agarrado de las telarañas. Corregida la ausencia de
  espacio tras la tirada de salvación en el encuentro de insectos.
- La estatua incluye una tabla pendiente de revisión independiente y un
  parámetro de título inglés pendiente de comprobar en presentación.
- Auditorías técnica y editorial sin errores.

### appendix-b-finalwild — Últimos encuentros generales de la selva

- Revisadas trece páginas (26 registros), con referencias físicas 198 y 202–205:
  cazador tabaxi, tigre, palma triflor, troll, introducción de muertos vivientes,
  vegepigmeos, hombres jabalí y tigre, paisaje invernal, trepadora y zombis,
  yuan-ti, Zhentarim y zorbos.
- Conservadas escolta sin pago, ausencia de encuentros hostiles y sus límites,
  así como persecuciones, captura y defensa del territorio.
- Paisaje invernal: mantenidos -30 grados Fahrenheit, como en el original
  exportado y el Anillo del Invierno revisado; el PDF convierte a Celsius.
- Auditorías técnica y editorial sin errores.

### appendix-b-omu — Omu, muertos vivientes y páginas de tablas

- Revisadas diez páginas narrativas y dieciséis páginas que insertan tablas
  (52 registros), con referencias físicas 195–199, 201, 203 y 205.
- Completadas las 116 páginas de diario del apéndice B. Esto no acredita las
  tablas ni los actores enlazados: se revisan como documentos independientes.
- Conservados umbral de encuentro 18, red compartida por dos gárgolas,
  rearmado de trampas por los kobolds y selección de objetivos del tumulario.
- Reconstruida la frase truncada del encuentro de gules con el PDF: el
  personaje con Percepción suficiente oye y huele a la manada que se acerca.
- Auditorías técnica y editorial sin errores. Los títulos internos de Embed
  en inglés siguen registrados como pendientes de presentación.

### appendix-b-smalltables — Exploradores, plantas, estatua y zombis

- Revisados 23 campos de cuatro tablas independientes, con referencias
  físicas 201 y 203. Incluye sus nombres y todos sus resultados.
- Conservadas las cantidades de plantas y zombis, la situación del grupo,
  el área y daño del glifo y el uso único de encontrar el camino.
- La estatua no puede volver a conceder el beneficio hasta el amanecer.
  Su comentario de probabilidad también requiere corrección funcional:
  fórmula del 75 % correcta, comentario inglés «result of 1» incorrecto.
- Auditorías técnica y editorial sin errores.

### appendix-b-supplies — Alijos, restos y tesoros

- Revisados 69 campos de tres tablas independientes, con referencias físicas
  197–199: veinte alijos, veinte exploradores muertos y veintiséis tesoros.
- Reconstruido el resultado 19 de alijos, truncado en «foldin» en el exportado:
  el PDF especifica dos tiendas, mesa de campaña y cuatro taburetes plegables.
- Corregidos «sin armadura» frente a «sin armas» y mordedura de serpiente
  frente a picadura. Conservados precios, cantidades, causas y pistas.
- Las flechas son bañadas en plata, como indica «silvered» en inglés. La
  cerradura conserva la CD duplicada del original, pendiente de revisar la
  presentación de su tirada en Foundry antes de eliminar la repetición.
- Auditorías técnica y editorial sin errores.

### appendix-b-terrain — Tablas por terreno de Chult y Omu

- Revisados nombres y resultados de doce tablas: nueve de Chult y tres de
  Omu, con referencias físicas 195, 196 y 205. Añadidos 423 registros.
- La mayoría de resultados son Embed sin texto traducible. Comprobado que
  todos apuntan a páginas existentes del apéndice B ya revisadas. Estos
  registros acreditan esa comprobación, no 423 traducciones nuevas de prosa.
- Sincronizadas las copias de exploradores y exploradores muertos que estaban
  escritas directamente en algunas tablas, conservando sus inserciones.
- Conservados los rangos y probabilidades originales; este bloque no acredita
  una comparación estadística entre ediciones ni una ejecución en Foundry.
- Cerrada la revisión de texto de los diarios y las diecinueve tablas nuevas
  del apéndice B, además de Puerto Nyanzaru, revisada previamente. Siguen
  pendientes actores enlazados y los problemas funcionales documentados.
- Auditorías técnica y editorial sin errores.

### appendix-d-link-verification — Corrección de las notas de enlaces

- Comprobado directamente en el exportado: `FDyn4HWR2JU4EFY6` es la página
  «Appendix D», con la introducción del apéndice, y `07OcWSNklHd1H0oT` es
  «Grungs». Se corrige la identificación errónea de las notas anteriores.
- Las referencias genéricas al apéndice D no necesitan redirigirse a las
  fichas individuales. No se han modificado UUID por esa suposición.
- Esta comprobación corrige el registro de incidencias; no añade campos a la
  revisión lingüística ni acredita el funcionamiento de los enlaces en Foundry.

### appendix-d-start — Introducción y primeras páginas de criaturas

- Revisadas seis páginas (12 registros): introducción del apéndice, Acererak,
  enanos albinos, aldani, almiraj y Artus Cimber. Referencias físicas 210–213 y 220.
- Revisados los ideales, vínculos y defectos de Acererak y Artus y el texto
  general de los enanos albinos. Aclarado que el orden alfabético es el inglés.
- Las biografías y perfiles insertados requieren revisión en sus actores;
  estas páginas no acreditan por sí solas la revisión de las fichas.
- Auditorías técnica y editorial sin errores.

### appendix-d-biographies-01 — Acererak, Artus y primeras criaturas

- Revisados 38 campos en ambas copias de seis actores: Acererak, guerrero
  enano albino, guerrero espiritual enano albino, aldani, almiraj y Artus Cimber.
  Incluye nombres, nombres de token, biografías y la referencia pública de Artus.
- Referencias físicas 210–213 y 220. Conservados historia y motivaciones,
  Almero, Anillo del Invierno, Alisanda y los compañeros de Artus.
- Zakhara se describe como tierra lejana, no como isla: el inglés dice «land».
  El guerrero espiritual recibe un sortilegio y conserva sus cinco conjuros.
- Sincronizado el texto general de los enanos con la página de diario revisada.
  Este bloque no acredita sus rasgos de combate, objetos ni actividades.
- Auditorías técnica y editorial sin errores.

### appendix-d-smalltraits — Textos completos de almiraj y aldani

- Revisados 30 campos adicionales en las dos copias de almiraj y aldani,
  con referencia física 211: alineamiento, rasgos, ataques, actividad y efecto.
- Comprobado por clave de campo que ambos actores tienen revisados todos sus
  textos exportados, sumando las biografías y nombres del bloque anterior.
- Conservados sentidos basados en oído o vista, respiración anfibia y un
  objetivo agarrado por cada pinza. El efecto del aldani conserva CD 11.
- Las fórmulas y datos mecánicos siguen siendo los originales; la cobertura
  textual completa no acredita su funcionamiento dentro de Foundry.
- Auditorías técnica y editorial sin errores.

### appendix-d-biographies-02 — Enredadera asesina y atropal

- Revisadas ambas copias de dos biografías y sus nombres, más las páginas de
  enredadera asesina, atropal y bodak: 18 registros; referencias 213–215 y 220.
- Conservadas dimensiones y características de la enredadera y el vínculo
  del atropal con el Plano Negativo, sus apariciones y la imposibilidad de
  resucitarlo. No se añaden conversiones métricas a las medidas del exportado.
- La biografía del bodak está vacía en el actor inglés, aunque existe texto
  en el PDF. La página solo lo inserta: no se acredita esa biografía como
  traducida ni se inventa un campo ausente; se registra la omisión del módulo.
- Auditorías técnica y editorial sin errores.

### appendix-d-vine-traits — Ataques de la enredadera asesina

- Revisados 26 campos de las dos copias del actor, con referencia física 220.
  Incluye alineamiento, Constreñir, Enmarañar, Apariencia Falsa y sus efectos.
- Conservados un solo objetivo constreñido, los estados agarrado y apresado,
  el daño al comienzo del turno y el área cuadrada de 15 pies de lado.
- Enmarañar permite gastar una acción para escapar y termina al morir la
  planta o usar de nuevo el rasgo; no se describe como un conjuro.
- Auditorías técnica y editorial sin errores. Pendiente ejecución en Foundry.

### appendix-d-atropal-traits — Acciones y auras del atropal

- Revisados 58 campos de ambas copias, con referencia física 214.
- Restaurado «celestial» en la nota de idiomas, respaldado por el PDF y por
  `languages.value` del actor. Corregido el título erróneo «Disrupt Life» a
  «Lamento»: descripción, salvación y coste de tres acciones lo identifican.
- Conservados recuperación de la mitad del daño, control exclusivo de las
  apariciones y pérdida del aura al cortar el cordón. Corregido «average»
  sobrante en la prosa del aura de energía negativa.
- Pendientes funcionales del original: Rayo de frío tiene alcance narrativo
  120 pies pero actividad con alcance `self` y tipo de ataque sin completar;
  Lamento también carece del alcance de 120 pies en su actividad. Los enlaces
  `[[/item Touch]]` y `[[/item Ray of Cold]]` usan nombres ingleses y requieren
  resolución por identificador para no depender del nombre traducido.
- Auditorías técnica y editorial sin errores.

### appendix-d-bodak — Rasgos y ataques del bodak

- Revisados los 28 campos de texto no vacíos de sus dos copias, con
  referencia física 215. El original no contiene biografía.
- Diferenciadas las dos miradas: una causa daño con salvación para mitad;
  la otra puede reducir a cero PG si se falla por cinco o más y no existe
  inmunidad a asustado. Conservados apartar la mirada y los efectos de la luz.
- El aura afecta al final del turno, se activa como acción adicional y
  excluye a muertos vivientes e infernales.
- Auditorías técnica y editorial sin errores. Pendiente ejecución en Foundry.

### appendix-d-bronto-champion — Brontosaurio y campeón

- Revisados 60 campos: los textos no vacíos de ambos actores en sus dos
  copias y sus páginas de diario, con referencias físicas 215 y 216.
- Conservados derribo del pisotón, ataque múltiple, repetición de salvación,
  recuperación de PG y variantes de ataque según los PG restantes.
- Completada la nota truncada de idiomas del campeón: uno cualquiera,
  normalmente común. La descripción de la armadura procede del exportado.
- Los actores originales no incluyen las biografías presentes en el PDF;
  queda registrada esta omisión, igual que en el bodak.
- Auditorías técnica y editorial sin errores. Pendiente ejecución en Foundry.

### appendix-d-chwinga-strider — Chwinga y caminante gigantesco

- Revisados 70 campos de los dos actores y sus páginas, con referencias
  físicas 215–217. Incluye biografía y cuatro conjuros del chwinga, cuyo
  texto completo se contrasta con el exportado inglés.
- Corregido «agua dulce» frente a «agua fresca». Conservados refugio en el
  propio espacio, visión ciega sin impedimentos, salida mediante acción,
  evasión y sortilegio sobrenatural a elección del DM.
- Conservados absorción de la mitad del daño de fuego y propagación por
  esquinas del estallido del caminante. Su biografía original está vacía.
- Auditorías técnica y editorial sin errores. Pendiente ejecución en Foundry.

### appendix-d-dinosaurs — Seis perfiles de dinosaurios

- Revisados 122 campos de seis actores en ambas copias y sus páginas:
  hadrosaurio, dimetrodón, estegosaurio, quetzalcoatlus, deinonychus y
  velocirraptor. Referencias físicas 218, 221, 223, 230 y 237.
- Conservados distancias de carga y picado, derribo, ataques adicionales y
  requisitos de Atacar en Manada. Corregida su etiqueta copiada «Baboon» en
  el velocirraptor, que no establece un requisito de juego aplicable al rasgo.
- Revisadas las biografías disponibles de estegosaurio y quetzalcoatlus;
  las de los otros cuatro actores están vacías en el exportado.
- Los enlaces por nombre `Bite`, `Claw` y `Claws` se incorporan al pendiente
  de resolución por identificador. Auditorías técnica y editorial sin errores.

### appendix-d-dragonbait — Dragonbait

- Revisados 46 campos de las dos copias del actor y su página, con referencias
  físicas 218 y 219. Incluye biografía, armas, armadura, escudo y rasgos.
- Conservados los nueve aromas y sus significados, amistad con Artus, estado
  Shen y límites de Sentir alineamiento. Restaurado «común» en la nota truncada
  de idiomas. Las descripciones de equipo se traducen del exportado inglés.
- Pendiente funcional comprobado: el enlace público a Artus usa el identificador
  `PDrrOhj8llUHrZ8e`, ausente del compendio exportado; el actor revisado de Artus
  tiene identificador `hNq59kIhDGqZBGXl`. El bloque de ideales, vínculos y defectos
  del PDF tampoco figura en la biografía ni en esta página del original.
- Auditorías técnica y editorial sin errores.

### appendix-d-eblis — Eblis

- Revisados 50 campos de las dos copias del actor y su página, con referencia
  física 219. Incluye biografía, ataques y tres conjuros innatos; sus descripciones
  completas se contrastan con el exportado inglés.
- Conservados los motivos de sus intercambios, los límites de sus ilusiones
  y las condiciones de sus conjuros. El enlace por nombre `Beak` queda incluido
  en el pendiente de resolución por identificador.

### appendix-d-firenewts — Salamandras flamígeras

- Revisados 122 campos: ambas copias de la guerrera y la bruja de Imix,
  incluidos sus textos de equipo y conjuros, y la página del diario.
  Referencias físicas 232 y 233; descripciones completas de conjuros y equipo
  contrastadas con el exportado inglés.
- Conservados descanso corto o largo para recuperar espacios, armadura de
  mago solo sobre sí misma y condiciones de daño de los conjuros. Las dos
  entradas originales de armadura de mago permanecen traducidas.
- El enlace por nombre `Scimitar` sigue pendiente de resolución por identificador.

### appendix-d-flail-snail — Caracol flagelo

- Revisados 48 campos de las dos copias del actor y su página, con referencia
  física 216. Conservados pérdida de tentáculos por turno, regeneración,
  cobertura total y condiciones de reflexión de conjuros.
- Discrepancia entre fuentes: el exportado contiene un rastro de vidrio y usos
  artesanales de la concha ausentes del PDF español. También fija su precio en
  5.000 po frente a las 2.500 po del PDF. Se conserva y traduce el exportado.
- Corregida la etiqueta errónea «+4 AC Bonud» del efecto de Defensa con concha.

### appendix-d-four-creatures — Mono, gárgola, tortuga y girallon

- Revisados 106 campos: cuatro páginas y ambas copias del mono volador,
  la gárgola gigante de cuatro brazos, la tortuga mordedora gigante y el girallon.
  Referencias físicas 221, 222, 228 y 234.
- Corregidos el enlace de encontrar familiar partido por el texto inglés y la
  etiqueta copiada «Baboon» del mono. Conservados los UUID y las tiradas.
- La tortuga se levanta mediante una prueba en el exportado; el PDF español
  indica una salvación. Se conserva la prueba original y se registra la diferencia.
- La biografía del girallon está vacía en el exportado. Los enlaces por nombre
  `Bite` y `Claw` siguen pendientes de resolución por identificador.

### appendix-d-froghemoth — Ranamot

- Revisados 64 campos de ambas copias del actor y su página, con referencia
  física 230. Conservados límites de tamaño, dos víctimas engullidas, agarre
  por tentáculo y duración de los efectos del daño de relámpago.
- Corregida la etiqueta textual «restrained» del enlace `prone` de regurgitación
  a «derribada», conforme al PDF y al identificador. Eliminado el «apply» suelto
  de la frase sobre escapar del cadáver.
- Pendiente funcional confirmado: el efecto `XK8sqMm3fnhW7ZEf` aplica realmente
  `restrained`, aunque describe la regurgitación. Se conserva su nombre Apresado
  para no ocultar qué estado aplica; corregir la automatización requiere otro bloque.
- La biografía original está vacía. El enlace por nombre `Bite` sigue pendiente.

### appendix-d-grungs — Grungs y variantes

- Revisados 286 campos: ambas copias de cinco actores y la página del diario.
  Incluye grung, guerrero verde, guerreros de élite dorado y naranja, y grung
  salvaje. Referencias físicas 222 y 223.
- Revisados conjuros, efectos del veneno por color, repeticiones de salvación,
  chirrido y saltos. La traducción conserva el contacto directo como impedimento
  para repetir la salvación contra Piel Venenosa.
- El exportado amplía la descripción del PDF con criaderos, ascenso de casta,
  esclavitud, dependencia del agua y variantes del veneno. Estos pasajes y los
  textos completos de los conjuros se traducen del inglés exportado.

### appendix-d-jaculi-kamadan — Jaculi y kamadan

- Revisados 76 campos de ambos actores en sus dos copias y sus páginas.
  Referencias físicas 224 y 225. Conservados los dos ataques adicionales de
  Abalanzarse y las condiciones para despertar del aliento somnífero.
- El exportado del jaculi omite en Salto la explicación del desplazamiento de
  30 pies, la ventaja tras saltar 10 pies y el daño adicional del PDF. Su campo
  solo contiene las tiradas de ataque y daño; se registra esta omisión funcional.
- Los enlaces por nombre `Bite`, `Claw` y `Snakes` siguen pendientes.

### appendix-d-kobolds — Inventor y hechicero escamoso kobold

- Revisados 146 campos de ambas copias de los dos actores y su página.
  Referencias físicas 225 y 226; textos completos de conjuros contrastados
  con el exportado. Ambos actores tienen la biografía vacía.
- Corregidos los espacios de 5 pies de lado frente a «5 pies cuadrados» del
  PDF, las etiquetas copiadas «Baboon» y el paréntesis erróneo junto a orbe
  cromático. Se conserva la ausencia de este conjuro como objeto del actor.
- El exportado de Puntos de Hechicería exige una acción adicional y omite en
  la descripción la recuperación tras descanso largo. Se conserva su contenido
  y se registra la diferencia con el PDF para revisar las reglas originales.
- Los comentarios de las tiradas de dispersión de ciempiés y avispas dicen
  «result of 1», aunque la fórmula usa 50 %. Se añaden al pendiente funcional.

## Balance de revisión editorial

- 783 páginas de texto revisadas: seis de la introducción, cien de los cuatro
  diarios del capítulo 1 (38 + 11 + 19 + 32), doce de reglas de viaje, 187 de
  localizaciones del capítulo 2, 49 de su índice, 88 del capítulo 3 y 37
  del capítulo 4, 126 del capítulo 5 y 178 de los apéndices A, B, C, D y F.
  No equivale a 783 páginas del PDF.
- 3777 registros editoriales comprobados contra originales y traducciones,
  incluidos los registros históricos parciales; no son 3777 campos distintos.
- La revisión de un diario con `@Embed` no acredita el contenido del documento
  insertado. Revisadas treinta y tres biografías en ambas copias de actores: siete
  príncipes y veintiséis criaturas o PNJ del apéndice D. Siguen pendientes las demás
  biografías y fichas, además de objetos, ayudas, escenas, interfaz y los
  diarios complementarios y apéndices todavía no cerrados.
- Auditorías estáticas y editorial sin errores. No se han renovado las
  instantáneas de Babele ni realizado una importación completa de Adventure.
- **La revisión del módulo continúa incompleta.** Siguen los documentos
  enlazados o insertados pendientes, diarios complementarios y apéndices.
- El informe v2 final solicitado queda pendiente hasta cerrar toda la revisión;
  este estado de avance no acredita una revisión completa ni la sustituye.

## Trabajo que sigue pendiente

- Revisar editorialmente el borrador contra el PDF, por capítulos y apéndices.
  La generación automática contiene expresiones poco naturales y puede cometer
  errores de sentido que las comprobaciones técnicas no detectan.
- Revisar nombres, terminología en contexto y etiquetas dentro de imágenes.
- Validar una importación completa de Adventure en un mundo limpio y comprobar
  las automatizaciones durante el juego. No sobrescribir el mundo existente.
- Preparar la publicación únicamente después de cerrar estas revisiones.

Todavía no se ha publicado una versión instalable con estos cambios.
