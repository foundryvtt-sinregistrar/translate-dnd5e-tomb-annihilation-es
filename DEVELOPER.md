# Desarrollo

## Estructura

- `module.json`: identidad, dependencias y versiones objetivo.
- `lang/es.json`: 126 claves de interfaz traducidas.
- `compendium/`: cinco packs con traducciones, incluidos borradores pendientes de revisión.
- `scripts/babele-register.js`: registro de traducciones para español en `setup`.
- `scripts/converters.js`: registro de convertidores con prefijo propio `toa`.
- `scripts/converters/toa-merge-by-id.js`: combinación por ID de actividades,
  efectos, avances, objetos de actores, tablas, páginas y etiquetas de escenas.
- `dev-tools/export/data/`: fuentes locales excluidas de Git.
- `tests/`: pruebas adaptadas de registro, idiomas y convertidores declarados.

Se reutiliza la infraestructura de DM 2024, basada en los módulos de traducción
existentes. Los mapeos se contrastan con exportaciones originales y con la ejecución de Babele.

## Reglas de edición

Traducir textos visibles conservando IDs, UUID, fórmulas, rutas, geometría y
campos mecánicos. En Foundry 14 los resultados de tablas usan `description`.
El convertidor de páginas acepta `text` y lo aplica a `text.content`.
Las macros solo preparan el nombre: no traducir ni reemplazar su código.

Babele local incluye soporte para colecciones de Adventure. Antes de añadir
entradas, exportar e identificar sus documentos anidados, comprobar los mapeos
que heredan y validar una importación de prueba. No asumir que traducir un
actor de su pack separado traduce también la copia incluida en la aventura.

No escribir en los compendios oficiales ni copiar sus bases de datos al módulo.
No distribuir PDF, OCR, exportaciones inglesas ni recursos del producto original.

## Comprobaciones

```sh
node --test tests/*.test.mjs
```

Estas pruebas comprueban el registro, los convertidores y la interfaz. Consultar
`dev-tools/translation/README.md` para las auditorías de contenido y de ejecución.
`.gitattributes` excluye herramientas, pruebas y documentación de desarrollo
de un futuro ZIP construido con `git archive`.
