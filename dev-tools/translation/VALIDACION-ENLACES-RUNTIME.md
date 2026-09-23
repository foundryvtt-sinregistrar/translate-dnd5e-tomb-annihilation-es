# Enlaces y secciones: comprobación en Foundry

23 de septiembre de 2026. Foundry 14.368, dnd5e 6.0.3, ToA 2.0.0,
Babele 2.9.1; mundo `DnD5e-6.0.3-Testing-Clean`, sesión GM.

Después de la importación limpia se detectaron cinco destinos del antiguo
compendio `book`, presente en diez campos. Sus diarios equivalentes existen
en el mundo importado. Se sustituyeron esas referencias por sus UUID reales.

Se corrigieron también 20 destinos con anclas inglesas, repartidos en 34 campos.
Tres localizaciones de Puerto Nyanzaru ahora tienen página propia; «Agentes del
Puño Ardiente» estaba en otra página. Los restantes saltos utilizan el ancla
del encabezado español, contrastada mediante `JournalEntryPage.buildTOC`.
Cada sustitución conserva una regla por campo en `confirmed-reference-repairs.json`.

`validate-absolute-links.mjs` terminó a las 18:25:17 UTC: **1.339 destinos
absolutos, incluyendo sus anclas, resueltos; cero fallos**. Se incluyen las
anclas del compendio de reglas del sistema. La prueba no certifica todos los
UUID relativos: estos requieren contexto documental.

La auditoría estática posterior resuelve 2.784 referencias locales y 1.880
comandos de objeto; conserva 1.142 referencias externas/contextuales y 41
apariciones de anclas. Cero regresiones detectadas.

Mediante `applyReviewedReferenceRepairs()` se actualizaron 39 campos del mundo
de pruebas, exigiendo que cada diferencia correspondiera exclusivamente a las
sustituciones documentadas. Se registraron los valores anteriores en consola.
La comprobación posterior, a las 18:25:20 UTC, dio **11.377 campos comprobados,
cero diferencias**, con 475 actores, 79 diarios y 42 escenas.

La importación inicial vacía corresponde al estado anterior a estas últimas
reparaciones. El resultado final incorpora una actualización controlada de
referencias; no se presenta como una segunda importación desde cero.
