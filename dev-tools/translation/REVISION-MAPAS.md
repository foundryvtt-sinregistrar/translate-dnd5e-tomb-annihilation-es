# Revisión visual de mapas

Fecha: 23 de septiembre de 2026. Fuentes: aventura original 2.0.0 y PDF español
aportado. La revisión inspecciona las imágenes, no solo los títulos traducidos
de las páginas.

## Atlas

Revisados sus 31 recursos. Incorporados 28 mapas/diagramas españoles mediante
`atlas-assets.json`. Comprobados visualmente todos los recortes generados, los
títulos, las leyendas y que no incluyan los párrafos contiguos del PDF.
Las tres imágenes conservadas son:

- Chult sin etiquetas: no contiene texto que traducir.
- Chult para jugadores: no contiene topónimos; conserva la rosa de los vientos.
- Puerto Nyanzaru para jugadores: conserva la unidad inglesa `feet` y las
  iniciales de la rosa de los vientos. Incidencia gráfica abierta; el mapa del
  DJ en español no es un sustituto adecuado por sus números y etiquetas.

Las páginas del atlas traducidas mantienen sus IDs. No cambian los permisos,
la geometría ni los fondos de las escenas. Se conservan las denominaciones
impresas en las imágenes oficiales españolas, incluida «Mina Wyrmheart».

## Fondos de las escenas

Inspeccionados los 38 archivos distintos usados por los niveles de las 42
escenas, incluidos fondo y niebla. Inventario y huellas en
`scene-image-review.json`. Se han encontrado rótulos ingleses en 14 archivos:

| Fondo | Texto restante |
| --- | --- |
| Villa de un príncipe mercante | Título y escala |
| Puerto Nyanzaru | Unidad `feet` |
| Mina Wyrmheart | Título y nombres de niveles |
| Yellyark | Tres leyendas del mecanismo de lanzamiento |
| Nueve santuarios de Omu, mapas individuales | Título de cada santuario |
| Omu | Unidad `feet` |

Los demás fondos carecen de prosa visible; varios conservan `W` en las rosas de
los vientos. No se contabiliza esa convención como prosa traducida.

Los fondos con incidencias quedan conservados y señalados. Su sustitución
requiere versiones para jugadores con dimensiones y encuadre idénticos, sin
números de zonas ni secretos. Los mapas del PDF incorporados al atlas son
versiones para el DJ y no cumplen esas condiciones. Esta revisión no acredita
una traducción integral de todos los píxeles del módulo.

## Validación

47 imágenes españolas en total: 19 ayudas y 28 recursos del atlas. Sus huellas
y correspondencias se comprueban con `audit_review_completion.py`. Las
expectativas de la siguiente importación contienen 11.377 comprobaciones,
incluida la carga de esas 47 imágenes. Todas cargaron correctamente en la
importación limpia del 23 de septiembre: véase `IMPORTACION-LIMPIA.md`.
