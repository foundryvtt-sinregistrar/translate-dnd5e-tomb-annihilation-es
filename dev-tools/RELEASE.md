# Publicar una release ligera

El workflow `.github/workflows/release.yml` sigue el procedimiento del PHB:
un push de un tag `v*` crea una **release en borrador** con notas automáticas.
El ZIP distribuido contiene solo traducción textual, sin imágenes ni fuentes PDF.

Referencia: [disparadores y filtros de tags de GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow).

## Preparación

1. Actualizar `module.json:version` y `CHANGELOG.md`; confirmar los cambios.
2. Comprobar localmente el paquete con
   `python dev-tools/build_light.py --release-tag v0.2.0` (adaptar la versión).
3. Desde el commit que se desea publicar, subir la rama y el tag:

   ```sh
   git push origin develop
   git tag -a v0.2.0 -m "Release 0.2.0"
   git push origin v0.2.0
   ```

   Si se publica desde otra rama, sustituir `develop`. No reutilizar un tag ya
   publicado: incrementar la versión. El workflow debe estar en el commit etiquetado.
4. En GitHub → Actions, comprobar la ejecución de **Release**.
5. En GitHub → Releases, revisar el borrador, sus notas y archivos, y pulsar
   **Publish release** cuando corresponda. El workflow no publica directamente.

## Archivos adjuntos

- `translate-dnd5e-tomb-annihilation-es.zip`: variante ligera.
- `module.json`: manifiesto generado, idéntico al incluido en el ZIP.
- `SHA256SUMS.txt`: comprobación del ZIP.

El manifiesto generado apunta al ZIP del tag exacto para evitar mezclar versiones.
Su URL de actualización es:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases/latest/download/module.json
```

Esta URL funciona después de publicar una release normal visible para el usuario;
no funciona con un borrador ni selecciona versiones marcadas como prerelease.
Para instalar una prerelease publicada, usar su manifiesto específico:
`https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases/download/v0.2.0/module.json`.
Un repositorio privado requiere acceso; una instalación pública desde Foundry
requiere que los archivos sean accesibles sin autenticación.

No usar el `module.json` sin procesar de la rama: describe el proyecto local
completo. Las URLs de distribución se incorporan al manifiesto de `dist/`.

## Validaciones

El workflow ejecuta las pruebas Node/Python, exige que el tag coincida con la
versión, restaura las 47 referencias de imágenes y comprueba el ZIP y su hash.
No necesita instalar Foundry ni disponer del producto oficial. En modo local
sin `--release-tag`, el constructor sigue comprobando la existencia de las
imágenes oficiales. La prueba de interfaz que necesita el original se omite
en CI si este no existe; no se presenta como validación de ejecución en Foundry.
