# Pruebas funcionales — 23 de septiembre de 2026

Entorno: Foundry 14.368, dnd5e 6.0.3, aventura 2.0.0;
mundo `DnD5e-6.0.3-Testing`, idioma español, sesión GM.

## Resultado reproducible

`validate-automations.mjs`, ejecutado mediante la macro del mundo a las
17:45:59 UTC: nueve comprobaciones correctas, cero errores.

- Las seis escenas reflejadas se encuentran por ID tras traducir sus nombres.
  Corregido el macro original, que buscaba «Mirrored» en el nombre. Se conserva
  el diálogo previo al restablecimiento y las fichas controladas por jugadores.
  La prueba no ejecuta el restablecimiento destructivo de las escenas.
- Trampa de tronco de la Mina Corazón de Sierpe, cortina negra, pasarela de
  Hrakhamar y luz de gas: activación, desactivación y estado original verificados.
- Obelisco de cieno: habilitación y deshabilitación del comportamiento de
  teletransporte verificadas. Esto no acredita aún el traslado de una ficha.
- Atropal, Toque: ataque `1d20 + 4 + 5` y daño `3d6` evaluados por el sistema.
- Valindra, Rayo de escarcha: daño `4d8` evaluado por el sistema. Restauradas
  las preferencias de la última tirada que guarda dnd5e en el objeto.
- Tabla Encuentros en Puerto Nyanzaru: tirada y resultado español comprobados.
  Las tiradas no publican mensajes ni consumen recursos.

## Interfaz de viaje

Prueba mediante los controles visibles: contador 20 → 21 → 20; lluvia ligera
→ tormenta tropical → lluvia ligera; terreno automático (costa, CD 10)
→ selva (CD 15) → automático. Aparece el control de tormenta tropical cuando
corresponde. Todos los textos de estos controles se muestran en español.

## Límites de la prueba

No hay un grupo principal con guía configurado en este mundo. No se acredita
con esta muestra la orientación con movimiento del grupo, las salvaciones de
sus miembros, todos los ataques/conjuros ni todas las regiones de la aventura.
Los resultados son pruebas funcionales representativas, no una partida completa.
