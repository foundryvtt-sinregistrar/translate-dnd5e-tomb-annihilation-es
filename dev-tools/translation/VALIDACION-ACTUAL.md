# Validación técnica: última sesión de Foundry y cierre estático posterior

Fecha: 23 de septiembre de 2026, 15:43 UTC.

**Actualización posterior:** la sesión de las 17:26–17:29 UTC en el mundo nuevo
renueva la validación de esquemas y comprueba la importación completa.
Consultar [VALIDACION-MUNDO-NUEVO.md](VALIDACION-MUNDO-NUEVO.md).

La sesión descrita abajo precede al cierre de objetos, metadatos, ayudas y
enlaces. No certifica los JSON actuales. El cierre estático posterior consta
en [CIERRE-TEXTUAL.md](CIERRE-TEXTUAL.md): 20154 campos revisados, 20158
registros editoriales válidos y 22 pruebas automatizadas superadas.

## Comprobaciones realizadas

- Foundry 14.368, dnd5e 6.0.3 y Babele 2.9.1, en sesión de GM.
- 698 documentos principales traducidos con mapeos de Babele construidos
  desde los JSON actuales y aceptados por los esquemas reales de Foundry.
- Cero errores de construcción o validación de esquemas.
- 15 pruebas Node y tres pruebas Python superadas.
- Auditorías estática y editorial sin errores; 19492 registros editoriales.
- La prueba de interfaz cubre las claves oficiales y sus parámetros de formato.

La ejecución usó `freshMappings: true`, `persist: false` e
`importPilot: false`. No actualizó los documentos de la aventura importada.
Se ha dejado la macro «ToA — Validación de traducción» en el mundo para
repetir esta comprobación. No publica mensajes en el chat.

## Límites y próximos pasos

- La primera ejecución intentó guardar las instantáneas, pero Foundry rechazó
  la subida de archivos. Se repitió correctamente sin persistirlas.
- Las instantáneas de `dev-tools/export/data` y la comparación completa de
  20154 campos descrita en `VALIDACION.md` corresponden a una ejecución anterior.
  No acreditan la versión actual. Falta renovar esa comparación completa.
- La aceptación por los esquemas no comprueba que cada enlace, tirada, trampa
  o teletransporte funcione durante el juego.
- El mundo abierto conserva texto del borrador anterior. Cambiar los JSON de
  Babele no actualiza automáticamente los documentos ya importados.
- Queda pendiente importar Adventure en un mundo limpio y probar allí las
  automatizaciones y enlaces. No sobrescribir la aventura del mundo existente.
- La revisión textual y de ayudas se ha cerrado posteriormente. La validación
  integral y el informe v2 final siguen pendientes.

## Repetir la comprobación

En una macro de tipo Script, desde una sesión de GM:

```js
const {validateRuntime} = await import(
  '/modules/translate-dnd5e-tomb-annihilation-es/dev-tools/translation/validate-runtime.mjs?review=20260923b'
);
const report = await validateRuntime({
  importPilot: false,
  freshMappings: true,
  persist: false
});
console.log(report);
```

Para renovar las instantáneas, hace falta que Foundry permita guardar archivos
en el directorio de exportación; entonces puede utilizarse `persist: true`
y ejecutar después `python dev-tools/translation/audit_runtime.py`.
