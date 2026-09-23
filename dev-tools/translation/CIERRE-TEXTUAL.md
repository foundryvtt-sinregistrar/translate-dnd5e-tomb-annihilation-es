# Cierre de los puntos 1, 2 y 3

Fecha: 23 de septiembre de 2026. Rama: `develop`.

## Resultado

- Punto 1: revisados los 180 objetos que quedaban; completados los 301 objetos independientes.
- Punto 2: completados 299 campos de metadatos, las 24 ayudas para jugadores y las 126 claves de interfaz.
- Punto 3: corregidas variantes terminológicas en 20 campos y enlaces por nombre en 154 campos. La auditoría conserva las incidencias heredadas para su comprobación en Foundry.

Los 20154 campos inventariados tienen un registro editorial de campo completo. Los 20158 registros incluyen revisiones históricas parciales; no representan campos distintos.

## Comprobaciones reproducibles

```powershell
python dev-tools/translation/audit_translation.py
python dev-tools/translation/audit_editorial.py
python dev-tools/translation/audit_review_completion.py
python dev-tools/translation/audit_links.py
node --test tests/babele-registration.test.mjs tests/translation-integrity.test.mjs
python -m unittest discover -s tests -p test_*.py
git diff --check
```

Auditorías de cobertura, sintaxis, HTML, números y hashes sin errores. Superadas 16 pruebas Node y seis Python. Los comandos de objetos usan IDs del inventario del propio actor; la auditoría solo admite esa sustitución si el nombre inglés coincide con un único objeto original.

## Referencias que requieren comprobación funcional

La auditoría resuelve 1870 comandos de objetos y 2749 referencias locales. Estas 19 referencias no encuentran destino en los datos exportados y ya aparecen así en el original. Pueden depender de documentos creados al importar o de errores del módulo base; no se han reasignado por aproximación.

| Campo | Referencia original |
|---|---|
| `dnd-tomb-annihilation.actors.1Gp38SRQcEPAsgSG.biographyPublic` | `Compendium.dnd-tomb-annihilation.actors.Actor.PDrrOhj8llUHrZ8e` |
| `dnd-tomb-annihilation.actors.HQJedCnkTg7qig36.items.07sdy4qaaW4MaB8W.description` | `.VzgFzcmocr1X1cp4` |
| `dnd-tomb-annihilation.actors.dbM4sT1yZLbnZR2a.items.FRnAjNB3QiDLVTFK.description` | `Touch` |
| `dnd-tomb-annihilation.actors.hNq59kIhDGqZBGXl.items.a34hmIKEi48x2E9h.description` | `.tAb7LaJZ0sNC1J0r` |
| `dnd-tomb-annihilation.actors.hiYoYWteYjF1umeT.items.fKIUImfcNk0pU2HN.description` | `.WZ3XGh48UoyAvBhS` |
| `dnd-tomb-annihilation.actors.hiYoYWteYjF1umeT.items.fKIUImfcNk0pU2HN.description` | `.PUYwkzEiKopyM6YL` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.dbM4sT1yZLbnZR2a.items.FRnAjNB3QiDLVTFK.description` | `Touch` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.1Gp38SRQcEPAsgSG.biographyPublic` | `Compendium.dnd-tomb-annihilation.actors.Actor.PDrrOhj8llUHrZ8e` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.hiYoYWteYjF1umeT.items.fKIUImfcNk0pU2HN.description` | `.WZ3XGh48UoyAvBhS` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.hiYoYWteYjF1umeT.items.fKIUImfcNk0pU2HN.description` | `.PUYwkzEiKopyM6YL` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.HQJedCnkTg7qig36.items.07sdy4qaaW4MaB8W.description` | `.VzgFzcmocr1X1cp4` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.actors.toaZaroumAlSarya.items.bLvq7KB0QTLkHbGE.description` | `Scimitar` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaAppBRandomEnc.pages.DFIxvfX6onZK3Yb1.text` | `Compendium.dnd-tomb-annihilation.actors.Actor.toaEncChwinga000` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaAppBRandomEnc.pages.gqmqw9126FVmMnBl.text` | `Actor.RliKw170F26yfIXb` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaAppBRandomEnc.pages.aTNpWLwHXTzBONVa.text` | `RollTable.dmgTreasureDrops` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaCh1PortNyanza.pages.oFthyTkEzX6AEeme.text` | `Item.toaCanoe00000000` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaCh2Hrakhamar0.pages.wBY2f0DUT7XgJJgZ.text` | `Macro.xjaIjor3WsKAz002` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaCh5TombOfTheN.pages.vvOmFAdbse9UvgMj.text` | `Actor.toaEncArtusCimbe` |
| `dnd-tomb-annihilation.adventures.OQ0bB1QgjuxagwGI.journals.toaCh5Level6Crad.pages.PzFdAiKV7ySB1BOE.text` | `Compendium.dnd-tomb-annihilation.items.Item.toaTalismanofthe` |

Además, 1168 referencias externas o contextuales y 47 anclas requieren resolución dentro de Foundry. La conservación de un UUID no demuestra que su destino exista o tenga el significado correcto.

## Alcance de las ayudas

Las 19 imágenes españolas se han inspeccionado tras su extracción; las cinco imágenes conservadas no requieren traducción de texto. La numeración y los IDs siguen Foundry, aunque los guías aparecen en distinto orden en el PDF español. Se conserva la mención a la fiebre del mono loco en el rumor de Salysa, distinta de la enfermedad revisada por Foundry.

Las ayudas no incluyen todos los mapas del atlas ni las imágenes de fondo de las escenas. Esas etiquetas siguen siendo un límite de la revisión integral.

## Siguiente fase

Renovar la comprobación de esquemas y las instantáneas, importar Adventure en un mundo limpio y comprobar enlaces, tiradas, trampas, teletransportes y controles. El mundo existente no se ha sobrescrito. El informe v2 final queda pendiente de esa validación integral.
