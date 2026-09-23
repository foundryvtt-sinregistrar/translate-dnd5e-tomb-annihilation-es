# Validación de la importación completa

23 de septiembre de 2026. Mundo `DnD5e-6.0.3-Testing`.
Foundry 14.368, dnd5e 6.0.3, Babele 2.9.1, idioma `es`.

## Resultado verificado

- Importación completa mediante el importador oficial: 475 actores, 79 diarios
  y 42 escenas. Las conversiones a monstruos y conjuros de 2024 estaban desactivadas.
- Activados el mapa de Chult y el diario de introducción en español.
- 11.349 comprobaciones contra los JSON revisados, sin diferencias tras la
  corrección descrita abajo: 11.330 campos importables y 19 rutas de imágenes.
  Incluye los nombres de las 41 carpetas; los tres campos generales del documento
  Adventure no se importan como documentos del mundo.
- Las 19 imágenes españolas cargan y se decodifican correctamente en el navegador.
- Nueva validación de los 698 documentos principales mediante los esquemas
  reales de Foundry: cero errores, ejecutada a las 17:26:23 UTC.
- Abierto el panel de seguimiento de la aventura: etiquetas, opciones de tiempo,
  terreno, amenaza, ritmo y controles de viaje en español. Esto acredita su
  presentación, no todas sus consecuencias mecánicas.

La comprobación posterior a la corrección terminó a las **17:29:34 UTC**.
La macro `ToA — Validación del mundo importado` queda guardada en el mundo.
Su versión guardada solo comprueba datos y escribe el resultado en consola;
no importa, repara ni publica mensajes en el chat.

## Incidencia corregida: nombres de fichas

La primera comparación detectó 28 diferencias, todas en nombres de fichas.
El hook `importAdventure` de Babele 2.9.1 sustituye el nombre de una ficha por
`actor.prototypeToken.name` cuando está activada la opción
`syncImportedAdventureTokenNames` y no hay nombre en ActorDelta.
Ejemplos: Nephyr se convertía en Aarakocra y Pirata en Bandido.

Se desactivó **Sync imported Adventure token names** en este mundo y se
restauraron únicamente los 28 nombres afectados mediante IDs de escena y ficha.
Antes de escribir, se comprobó que cada diferencia coincidía exactamente con
el nombre de prototipo que Babele habría aplicado. No se modificaron posiciones,
actores, características, reglas o datos del otro mundo.

El README incluye esta configuración necesaria antes de futuras importaciones.
No se ha repetido una importación desde cero con el ajuste desactivado; el
resultado de cero diferencias corresponde a la importación reparada.

## Referencias heredadas confirmadas sin destino

Se intentó resolver en el mundo nuevo los ocho UUID distintos que aparecían
en nueve campos de la auditoría estática. Los ocho siguen sin destino:

- `Compendium.dnd-tomb-annihilation.actors.Actor.PDrrOhj8llUHrZ8e`
- `Compendium.dnd-tomb-annihilation.actors.Actor.toaEncChwinga000`
- `Actor.RliKw170F26yfIXb`
- `RollTable.dmgTreasureDrops`
- `Item.toaCanoe00000000`
- `Macro.xjaIjor3WsKAz002`
- `Actor.toaEncArtusCimbe`
- `Compendium.dnd-tomb-annihilation.items.Item.toaTalismanofthe`

Los diez comandos de objetos restantes de la auditoría estática no se han
certificado mediante interacción. Tampoco se han certificado aún todas las
referencias externas, las anclas ni las automatizaciones de trampas y viajes.

## Reproducción

En el repositorio, ejecutar primero:

```powershell
python dev-tools/translation/audit_links.py
python dev-tools/translation/prepare_world_validation.py
```

Desde una macro Script en el mundo de pruebas, como GM:

```js
const {validateImportedWorld} = await import(
  '/modules/translate-dnd5e-tomb-annihilation-es/dev-tools/translation/validate-imported-world.mjs'
);
await validateImportedWorld();
```

Las expectativas se generan en la carpeta local excluida de Git. El validador
rechaza otro título de mundo. La función opcional `restoreReviewedTokenNames`
no se ejecuta automáticamente y solo permite reparar nombres que coinciden con
el resultado de la sincronización de Babele.

Las instantáneas antiguas no se han sustituido. Esta sesión usó `persist:false`
para la validación de esquemas y comprobó los documentos importados directamente.
El informe v2 final sigue pendiente de cerrar las incidencias funcionales y
las etiquetas de mapas restantes.
