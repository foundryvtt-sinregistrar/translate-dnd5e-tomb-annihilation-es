# La tumba de la aniquilación — Español (Babele)

Versión de prueba `0.2.0` del módulo `translate-dnd5e-tomb-annihilation-es`.
Incluye traducción de los cinco compendios y 126 textos de interfaz.
**Revisión textual cerrada; validación funcional en curso.** No es una edición final ni
una publicación instalable desde una URL remota. El ZIP local se instala
extrayendo su carpeta en `Data/modules/` con Foundry detenido.

## Entorno objetivo

- Foundry VTT 14.368 y dnd5e 6.0.3.
- Babele 2.9.1 y sus dependencias.
- Módulo oficial `dnd-tomb-annihilation` 2.0.0 instalado y activo.

La carga de Babele, los esquemas y la importación completa se han comprobado
en este entorno. Véase [la validación del mundo nuevo](dev-tools/translation/VALIDACION-MUNDO-NUEVO.md)
para los resultados y las incidencias funcionales pendientes.

## Instalación local

1. Mantener esta carpeta en `Data/modules/translate-dnd5e-tomb-annihilation-es`.
2. Reiniciar Foundry para que reconozca el módulo nuevo.
3. Activar Babele, el módulo oficial y esta traducción.
4. Seleccionar español y recargar el mundo.
5. Antes de importar, desactivar en Babele **Sync imported Adventure token names**.
   La aventura ya incluye nombres revisados para cada ficha. Esa sincronización
   los sustituye por nombres genéricos del actor y puede ocultar nombres de PNJ.

El registro de Babele espera a `setup`, cuando existe `core.language`, y se
limita a español y variantes regionales. Los documentos que ya estaban
importados en un mundo no se sustituyen automáticamente al activar el módulo.

## Compendios preparados

| Archivo dentro de `compendium/` | Tipo |
|---|---|
| `dnd-tomb-annihilation.adventures.json` | Adventure |
| `dnd-tomb-annihilation.actors.json` | Actor |
| `dnd-tomb-annihilation.items.json` | Item |
| `dnd-tomb-annihilation.tables.json` | RollTable |
| `dnd-tomb-annihilation.macros.json` | Macro |

La lista procede del manifiesto del módulo oficial local. Los diarios y escenas
deben inventariarse dentro de la aventura: no se han inventado packs separados.
La traducción de Adventure incluye 475 actores, 79 diarios con 1.033 páginas,
42 escenas y 41 carpetas. También cubre textos de modificaciones locales de
fichas. Los nombres propios y los fragmentos puramente técnicos pueden coincidir
con el original. Las ayudas para jugadores incluyen 19 imágenes españolas;
el atlas incorpora otros 28 mapas y diagramas españoles. Quedan rótulos
ingleses en 14 fondos de escena y la escala del mapa de Puerto Nyanzaru para
jugadores. Las pruebas no cubren todas las automatizaciones de una partida.

## Desarrollo

### Paquete ligero, solo texto

Ejecutar `python dev-tools/build_light.py` para generar en `dist/` el ZIP
`translate-dnd5e-tomb-annihilation-es-0.2.0-light.zip`. Conserva la traducción
textual y recupera las 47 rutas de imágenes del módulo oficial, sin incluir
imágenes ni modificar la variante completa. Requiere el módulo oficial local
para comprobar que existen esos recursos.

Ambas variantes tienen el mismo identificador y versión: son alternativas de
instalación. Los documentos ya importados no se actualizan automáticamente;
probar la variante ligera mediante una importación nueva si el mundo anterior
utilizaba las imágenes españolas.

Consultar [DEVELOPER.md](DEVELOPER.md) y [ROADMAP.md](dev-tools/ROADMAP.md).

```sh
node --test tests/*.test.mjs
```

Repositorio: [foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es).
Todavía no hay una publicación ni URLs de instalación configuradas.
Los PDF EN/ES ya están procesados para consulta local; consultar
[la guía de referencias](dev-tools/export/README.md) y
[el estado de traducción](dev-tools/translation/ESTADO-TRADUCCION.md).
Los PDF, OCR y exportaciones se guardan en `dev-tools/export/data/`, excluidos
de Git y del paquete de distribución.

Traducción no oficial, sin afiliación con Wizards of the Coast ni Foundry VTT.
Requiere el contenido oficial y no incluye sus bases de datos. Las imágenes
españolas de las ayudas proceden del PDF aportado; véase su
[nota de procedencia](assets/handouts/es/README.md).
