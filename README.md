# La tumba de la aniquilación — Español (Babele)

Esqueleto del módulo `translate-dnd5e-tomb-annihilation-es`, versión `0.1.0`.
No contiene entradas traducidas
ni constituye una publicación instalable desde una URL remota.

## Entorno objetivo

- Foundry VTT 14.368 y dnd5e 6.0.3.
- Babele 2.9.1 y sus dependencias.
- Módulo oficial `dnd-tomb-annihilation` 2.0.0 instalado y activo.

Las versiones del manifiesto son el objetivo del esqueleto. La carga y la
importación de la aventura todavía deben comprobarse dentro de Foundry.

## Instalación local

1. Mantener esta carpeta en `Data/modules/translate-dnd5e-tomb-annihilation-es`.
2. Reiniciar Foundry para que reconozca el módulo nuevo.
3. Activar Babele, el módulo oficial y esta traducción.
4. Seleccionar español y recargar el mundo.

El registro de Babele espera a `setup`, cuando existe `core.language`, y se
limita a español y variantes regionales. Solo hay plantillas vacías; el contenido
de la aventura seguirá en inglés hasta incorporar las traducciones.

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
La plantilla de aventura prepara nombre, descripción y leyenda; falta contrastar
la traducción de sus colecciones anidadas con una exportación real.

## Desarrollo

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
Requiere el contenido oficial; este esqueleto no incluye sus datos ni recursos.
