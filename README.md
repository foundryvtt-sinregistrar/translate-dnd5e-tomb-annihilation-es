# La tumba de la aniquilación — Solo texto — Traducción al español

**Español** | [English](README.en.md)

Traducción para Foundry VTT mediante Babele. Identificador: `translate-dnd5e-tomb-annihilation-es`.

## Estado

Versión: **0.2.1**. Variante de prueba solo texto. Incluye cinco compendios y 126 claves de interfaz. La revisión textual consta como cerrada en los informes del proyecto; la validación funcional integral sigue pendiente. El paquete sustituye 47 rutas de imágenes españolas por las del módulo oficial y no incluye imágenes. Los rótulos de esas imágenes permanecen en su idioma original.

Consulta [CHANGELOG.md](CHANGELOG.md).

## Requisitos

Versiones declaradas en el manifiesto; «—» indica que no se declara ese límite.

| Dependencia | Mínima | Verificada |
|---|---|---|
| Foundry VTT | 14.368 | 14.368 |
| dnd5e | 6.0.3 | 6.0.3 |
| babele | 2.9.1 | — |
| dnd-tomb-annihilation | 2.0.0 | — |

Instala y activa las dependencias, adquiriendo por separado los productos oficiales cuando sean necesarios.

Antes de importar, desactiva en Babele **Sync imported Adventure token names**. Las variantes completa y solo texto comparten identificador: no se instalan como módulos distintos. Usa una importación nueva en un mundo de prueba para comprobar esta variante. La variante completa necesita recursos españoles que no están versionados; su reconstrucción no está disponible con este clon.

## Instalación

En la configuración de Foundry, abre **Add-on Modules → Install Module** y utiliza este manifiesto:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases/latest/download/module.json
```

Para instalar manualmente, descarga `translate-dnd5e-tomb-annihilation-es.zip` de las [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases). Con Foundry detenido, extrae la carpeta `translate-dnd5e-tomb-annihilation-es` en `Data/modules/`; el manifiesto debe quedar en `Data/modules/translate-dnd5e-tomb-annihilation-es/module.json`.

## Activación

1. Abre un mundo dnd5e.
2. Activa Babele, sus dependencias, los productos oficiales requeridos y esta traducción.
3. Selecciona **Español** y recarga el mundo.
4. Abre un compendio traducido para comprobar el resultado.

El registro es automático para `es` y sus variantes regionales. Otros idiomas no activan la traducción española.

## Actualización

Actualiza desde Foundry o sustituye la carpeta con el ZIP publicado y Foundry detenido. Recarga el mundo. Las copias ya importadas no se sincronizan automáticamente: revisa las diferencias antes de sustituir documentos con cambios propios.

## Contenido incluido

- `dnd-tomb-annihilation.actors.json`.
- `dnd-tomb-annihilation.adventures.json`.
- `dnd-tomb-annihilation.items.json`.
- `dnd-tomb-annihilation.macros.json`.
- `dnd-tomb-annihilation.tables.json`.

## Limitaciones

La cobertura textual y las pruebas automáticas no acreditan todas las automatizaciones de una partida. Conserva las limitaciones indicadas en Estado. Las copias importadas no se actualizan automáticamente. Las nuevas URLs de release necesitan una publicación con sus adjuntos; mientras no estén disponibles, utiliza un ZIP validado. No se distribuyen fuentes privadas, PDF, OCR ni exportaciones oficiales completas.

## Soporte y contribuciones

Comunica errores en las [incidencias](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/issues), indicando versiones, compendio/documento afectado, pasos, resultado esperado y observado, y si se trata de una copia importada.

## Desarrollo

La [guía de desarrollo](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/blob/main/DEVELOPER.md) está disponible en el repositorio y se excluye del ZIP instalable.

## Licencia y créditos

Las aportaciones propias de `foundryvtt-sinregistrar` se ofrecen bajo la licencia [MIT](LICENSE.md), con el alcance allí indicado. El contenido original traducido y los demás materiales de terceros conservan sus derechos y condiciones; MIT no concede permisos adicionales sobre ellos.

Traducción no oficial, sin afiliación con Wizards of the Coast ni Foundry VTT. Los materiales del producto oficial pertenecen a sus respectivos titulares. Autor del módulo: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).
