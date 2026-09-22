# Flujo de traducción

## Preparación y generación

Desde la carpeta del módulo:

```powershell
python dev-tools/translation/inventory.py
python dev-tools/translation/generate_draft.py
python dev-tools/translation/reuse_verified.py
python dev-tools/translation/apply_pilot.py
python dev-tools/translation/configure_mappings.py
python dev-tools/translation/audit_translation.py
```

El generador usa el modelo local OPUS-MT EN/ES y CTranslate2 del módulo vecino
`translate-dnd5e-dm-2024-es/tmp/`. No envía los textos a servicios externos.
Para preparar ese entorno en otro equipo, usar las instrucciones y herramientas
de `translate-dnd5e-dm-2024-es/dev-tools/translation/prepare_local_mt.py`.
Esta dependencia es exclusiva de desarrollo: Foundry solo necesita los JSON y
scripts del módulo. Las auditorías no requieren el modelo.

`reuse_verified.py` aprovecha los archivos bilingües `*.reference.json` del
módulo vecino únicamente si coincide el texto inglés y se preservan los tokens
técnicos y cifras. Las coincidencias ambiguas no se aplican.

`reviewed-segments.json` y `terminology.json` contienen correcciones y términos
revisados. `apply_pilot.py` aplica equivalencias exactas y el texto de Cuenca
Aldani adaptado del PDF español. `generate_draft.py --refresh` actualiza solo
campos cuyo contenido aún coincide con la huella del borrador registrado;
conserva correcciones manuales y reutilizaciones. La caché y procedencia están
en `export/data/`, excluidas de Git.

La lista `review` de `mt-provenance.json` conserva avisos históricos del modelo.
La auditoría actual, `translation-audit.json`, determina cuáles siguen presentes.
Los cambios de fórmulas, enlaces, etiquetas HTML o cifras hacen fallar la auditoría.

## Validación en Foundry

Con Babele y esta traducción activos, ejecutar como GM:

```js
await game.babele.refreshTranslationSources();
const {validateRuntime} = await import("/modules/translate-dnd5e-tomb-annihilation-es/dev-tools/translation/validate-runtime.mjs");
await validateRuntime({importPilot: true});
```

Comprueba la traducción de los cinco packs con Babele y construye los documentos
usando los esquemas reales de Foundry. Guarda instantáneas locales antes y después
de la normalización de Foundry. La comparación mecánica usa la instantánea anterior
para distinguir traducción y migraciones automáticas del sistema.

Con `importPilot: true`, crea un diario, una escena, un actor, un objeto y una tabla
en carpetas «ToA — Pruebas de traducción». Las repeticiones reutilizan esas copias.
No reemplaza documentos previos ni activa la escena de prueba. Estas creaciones
individuales no equivalen a reimportar la aventura completa.

```powershell
python dev-tools/translation/audit_runtime.py
node --test tests/*.test.mjs
python -m unittest discover -s tests -p 'test_*.py'
```

Después de modificar convertidores, recargar Foundry; actualizar únicamente los
JSON permite refrescar las fuentes de Babele. Repetir la validación si cambia el
contenido: las instantáneas corresponden a una ejecución concreta.

## Revisión editorial

La cobertura técnica completa no implica revisión lingüística completa. Revisar
los borradores por diario y contrastarlos con la edición española, conservando
las diferencias mecánicas de Foundry. El siguiente trabajo editorial prioritario
es la introducción y Puerto Nyanzaru, seguidos por los capítulos 2-5 y apéndices.
Los textos integrados en imágenes siguen siendo los del recurso original.

El avance por lotes se documenta en `ESTADO-TRADUCCION.md`.
`editorial-review.json` registra las rutas, referencias y huellas SHA-256 de los
campos revisados en esos lotes. Las huellas identifican la versión revisada;
no deben interpretarse como una aprobación de cambios posteriores del texto.
Las equivalencias se conservan en `reviewed-segments.json` para su reutilización.

Cuando una entrada editorial incluye `scope.type = prefix-before-marker`, solo
está revisado el fragmento anterior al marcador indicado, que queda excluido.
Las huellas se calculan sobre ese fragmento, no sobre el campo completo. Las
equivalencias parciales no se aplican con `apply_pilot.py`, que solo reemplaza
campos completos por coincidencia exacta; deben incorporarse con su contexto.

`scope.type = between-markers` delimita una sección interna: se incluye el
marcador de inicio y se excluye el de final. Las huellas se calculan solo sobre
esa sección. Los límites ingleses y españoles se registran por separado.
