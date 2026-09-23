# Importación limpia verificada

Fecha: 23 de septiembre de 2026. Mundo: `DnD5e-6.0.3-Testing-Clean`.
Foundry 14.368, dnd5e 6.0.3, Tomb of Annihilation 2.0.0, Babele 2.9.1.

## Condiciones previas

La macro de comprobación registró a las 18:08:01 UTC:

```json
{"world":"DnD5e-6.0.3-Testing-Clean","language":"es","sync":false,"actors":0,"journals":0,"scenes":0}
```

Activados seis módulos: aventura original, traducción de la aventura, Babele,
libWrapper y traducciones españolas del núcleo y dnd5e. Desactivada la opción
`babele.syncImportedAdventureTokenNames` antes de importar.

Importación desde la hoja de la aventura traducida. Activada la escena inicial;
sin mostrar el diario de primeros pasos, sin convertir monstruos/conjuros a
2024 y sin personalizar los detalles del mundo.

## Resultado

`validateImportedWorld()` comenzó a las 18:09:37 UTC y completó su informe a
las 18:09:48 UTC:

| Comprobación | Resultado |
| --- | --- |
| Actores | 475 esperados, 475 importados |
| Diarios | 79 esperados, 79 importados |
| Escenas | 42 esperadas, 42 importadas |
| Campos y rutas de imágenes | 11.377 comprobaciones, cero diferencias |
| Imágenes españolas | 47 cargadas; cero errores de decodificación |
| Destinos UUID corregidos, sin duplicados | 8 de 8 resueltos |
| Sincronización de nombres de Babele | Desactivada antes y después |

Los ocho destinos son Artus Cimber en compendio y mundo, chwinga, troll,
tabla Tesoros obtenidos, canoa, macro Alternar la pasarela y Talismán de la esfera.
Las correcciones de referencias relativas de objetos están verificadas por la
auditoría local; no se confunden con estos ocho UUID absolutos.

No se ejecutó `restoreReviewedTokenNames()` ni se repararon nombres después de
esta importación. Queda reproducida la solución al problema observado en el
primer mundo, donde Babele había sustituido 28 nombres.

Esta prueba acredita los textos y recursos importados, no una partida completa
ni todos los efectos mecánicos del sistema. Las pruebas funcionales se detallan
en `VALIDACION-AUTOMATIZACIONES.md` y las incidencias gráficas en `REVISION-MAPAS.md`.
