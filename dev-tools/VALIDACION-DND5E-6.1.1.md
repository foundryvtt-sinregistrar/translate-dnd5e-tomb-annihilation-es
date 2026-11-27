# Validación de La tumba de la aniquilación con D&D5e 6.1.1

Fecha: 2026-11-27. Rama local: `compat/dnd5e-6.1.1`.

## Entorno y aislamiento

Foundry VTT 14.370, dnd5e 6.1.1, Babele 2.9.1, producto oficial 2.0.0 y
traducción 1.14.2 con los cambios locales de esta rama. Idioma: español.
Se usó el importador nativo en `qa-dnd5e611-adventures`, copia del mundo
`dnd5e-606`. No había colisiones con los documentos previos ni con los de
Phandelver. El mundo original no recibió importaciones.

## Resultado de importación y persistencia

| Tipo | Esperados | Importados y conservados tras recargar |
| --- | ---: | ---: |
| Actores | 475 | 475 |
| Diarios | 79 | 79 |
| Escenas | 42 | 42 |
| Carpetas | 41 | 41 |

Adventure no contiene objetos, tablas ni macros independientes; esos tipos
del producto existen en sus otros compendios y no se cuentan como ausentes.
Todos los documentos importados pasan el esquema real de Foundry. No hay
diferencias de nombres guardados, etiquetas de fichas ni actores de ficha
sin destino. Los 11.330 campos de texto comparados con el Adventure traducido
antes de importar coinciden exactamente.

Se importó todo sin las conversiones opcionales de monstruos o conjuros 2024.
Para comprobar el arreglo se retiraron los actores y escenas de esta aventura
en QA y se repitió la importación: recreó esos documentos, actualizó los demás
y mantuvo sus IDs. En esa repetición se desactivó conservar la ficha del grupo,
porque se había retirado también su Actor para probar el alta completa.

Se mostraron Mapa de Chult y el diario Introducción en español. Desde Resumen
de la historia se pulsó el enlace de Ras Nsi y se abrió su ficha importada con
sus rasgos traducidos. La imagen de escena Ataaz Muhahah devolvió HTTP 200.
Esta muestra no equivale a revisar todas las imágenes o automatizaciones.

## Corrección de etiquetas de fichas

La primera importación dejó 28 etiquetas diferentes de las revisadas,
por la sincronización asíncrona de nombres de actor de Babele: por ejemplo
Nephyr → Aarakocra y Pirata → Bandido.

`scripts/adventure-import.mjs`, cargado desde `scripts/babele-register.js`,
registra un `postImport` únicamente para esta aventura y español/variantes.
Restaura las etiquetas del Adventure en escenas creadas o actualizadas mediante
`updateEmbeddedDocuments` con `diff:false`, escribiendo solo `_id` y `name`.
El valor actual puede aún coincidir mientras la escritura de Babele está
pendiente; por eso no se omiten coincidencias ni se permite que Foundry
descarte la escritura final. La nueva importación y la recarga dejan cero
etiquetas distintas del documento traducido.

## Incidencias heredadas del original

Comprobadas 1.534 referencias distintas: una no resuelve. Es la referencia
relativa `.sL2AvID05bmeUbdH` en
`Actor.hNq59kIhDGqZBGXl.Item.vondFRpZLaZBG1NF`. La referencia ya figura en el
objeto inglés y ese ID no existe entre sus objetos embebidos originales.

Una nota de Mapa de Wyrmheart (`toaWyrmheartMine`, nota `aMIs0Wvp5Vam83Oz`)
apunta a la página ausente `bixoWjqSFmaKwq1V` del diario homónimo. El mismo
destino está en la escena inglesa y la página tampoco existe en su diario.

El grupo `toaParty00000000` referencia al Actor ausente `t56dY1HPaCL7iZq5`.
Se confirmó que esa referencia también está en los datos ingleses. Se conservan
estas incidencias como evidencia; no se modifican compendios oficiales para
ocultarlas. No hay referencias rotas nuevas atribuidas a la traducción.

Pruebas locales: 23 Node y 54 Python, todas superadas. Las regresiones cubren
el nombre que aún coincide mientras hay sincronización pendiente, `diff:false`,
escenas actualizadas y la restricción por aventura e idioma.

Las instantáneas privadas están en `export/data/qa-611-import.json`,
`qa-611-field-diff.json` y `qa-611-references.json`, excluidos de Git.

## Reanudación

- Importación completa y persistencia: PASS, con las excepciones heredadas indicadas.
- `verified` pasa a 6.1.1; la versión publicada no cambia.
- Los documentos importados permanecen en la copia QA para revisión.
- La revisión editorial e imágenes y las pruebas exhaustivas de juego siguen siendo trabajos distintos.
- Validación preparada para integración local en main; sin push, tag ni release.
