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

## Trabajo que sigue pendiente

- Revisar editorialmente el borrador contra el PDF, por capítulos y apéndices.
  La generación automática contiene expresiones poco naturales y puede cometer
  errores de sentido que las comprobaciones técnicas no detectan.
- Revisar nombres, terminología en contexto y etiquetas dentro de imágenes.
- Validar una importación completa de Adventure en un mundo limpio y comprobar
  las automatizaciones durante el juego. No sobrescribir el mundo existente.
- Preparar la publicación únicamente después de cerrar estas revisiones.

Todavía no se ha publicado una versión instalable con estos cambios.
