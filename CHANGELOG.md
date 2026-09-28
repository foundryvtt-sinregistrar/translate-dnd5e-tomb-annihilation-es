# Changelog

Las nuevas entradas se redactan en español, bajo `[Unreleased]` y las categorías `Added`, `Changed` y `Fixed`. El historial anterior conserva su contenido e idioma.


## [Unreleased]

## [0.2.1] - 2026-09-28

- Comprobados en Foundry 698 documentos, nombres y campos explícitos; importada y revisada una muestra. Evidencia y límites en `dev-tools/homogeneizacion/VALIDACION-FOUNDRY.md`.

- Adoptada la licencia MIT para las aportaciones propias de foundryvtt-sinregistrar, conservando los derechos y condiciones de terceros.

### Changed

- Homogeneizados documentación ES/EN, guía de desarrollo, configuración de edición, exclusiones y proceso de distribución. Constructor desde un único commit, perfil por proyecto, manifiesto externo, SHA-256 y validación compartida en PR y releases. Se conservan las particularidades y los avisos de licencia del proyecto.


- Workflow de GitHub Actions para crear releases en borrador al subir tags `v*`.
- Empaquetado ligero compatible con CI, manifiesto instalable y SHA-256.
- Validación de coincidencia entre tag y versión, y prueba del paquete sin Foundry.

## [0.2.0] — 2026-09-23 — Versión de prueba local

- Revisión editorial completa de 20.154 campos y 126 claves de interfaz.
- 19 ayudas y 28 mapas/diagramas en español.
- Reparaciones de enlaces retirados y anclas españolas verificadas en Foundry.
- Corrección del restablecimiento de escenas reflejadas mediante IDs.
- Importación limpia validada y 11.377 comprobaciones sin diferencias tras
  aplicar las últimas reparaciones de enlaces al mundo de pruebas.
- 1.339 destinos absolutos y sus anclas resueltos, 19 pruebas Node y ocho Python.
- Pendientes: rótulos ingleses en 14 fondos y una escala del atlas, pruebas
  funcionales exhaustivas y diagnóstico de los avisos de consola documentados.
- Paquete local; no se publica una release remota ni se configura actualización automática.

## [0.1.0] — Borrador inicial (histórico)

- Esqueleto `0.1.0` para Foundry VTT 14.368 y dnd5e 6.0.3.
- Dependencias Babele y `dnd-tomb-annihilation`.
- Cinco plantillas vacías ajustadas a los packs del módulo oficial 2.0.0.
- Registro para español y convertidores por ID con prefijo `toa`.
- Documentación, exclusiones de distribución y pruebas de registro.
- Referencias PDF EN/ES procesadas localmente, con extracción por página y OCR
  selectivo; herramienta reproducible y guía de consulta incluidas.
- Identificador corregido a `translate-dnd5e-tomb-annihilation-es`.
- Exportación original de los cinco packs y catálogo de campos anidados.
- Borrador de traducción de 20.154 campos y 126 claves de interfaz en español.
- Glosario, reutilización verificada, auditorías y herramientas de generación local.
- Convertidores de carpetas, actores y modificaciones de fichas de Adventure.
- Validación con Babele y esquemas de Foundry; cinco documentos de prueba.
- Pendientes revisión lingüística completa, importación integral en mundo limpio
  y primera publicación.

## Version Links

[Unreleased]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases/tag/v0.2.1
