# Informe de revisión v2

Fecha: 23 de septiembre de 2026. Rama: `develop`.
Módulo: `translate-dnd5e-tomb-annihilation-es`, versión 0.1.0.
Entorno probado: Foundry 14.368, dnd5e 6.0.3, aventura 2.0.0 y Babele 2.9.1.

## Dictamen

La revisión editorial de los campos inventariados está cerrada. Se han
completado la inspección de recursos gráficos, la importación en un mundo
vacío y las pruebas funcionales representativas descritas abajo. Se entrega
este informe con incidencias abiertas: **no certifica una versión final
completamente traducida ni todas las automatizaciones de una partida**.

## Cobertura y resultados

| Área | Resultado verificado |
| --- | --- |
| Texto | 20.154/20.154 campos con revisión completa; 20.158 registros editoriales y cero errores de integridad |
| Interfaz | 126 claves cubiertas, conservando parámetros |
| Documentos | 698 documentos principales comprobados con los conversores y esquemas reales; cero errores |
| Importación vacía | 475 actores, 79 diarios y 42 escenas; 11.377 comprobaciones sin diferencias |
| Imágenes españolas | 19 ayudas y 28 mapas/diagramas; 47 recursos cargados correctamente |
| Inspección gráfica | 31 imágenes del atlas y 38 fondos distintos de escenas revisados |
| Enlaces estáticos | 2.784 referencias locales y 1.880 comandos de objeto resueltos; cero regresiones |
| Enlaces en Foundry | 1.339 destinos absolutos, incluidas anclas, resueltos; cero fallos |
| Pruebas automatizadas | 19 pruebas Node y ocho Python superadas; `git diff --check` sin errores |
| Funcionalidad | Nueve comprobaciones representativas y controles visibles de día, clima y terreno |

Los campos idénticos al inglés incluyen nombres propios y contenido técnico;
no se exige modificarlos artificialmente. La cobertura editorial acredita el
registro de revisión, no elimina la posibilidad de erratas futuras.

## Correcciones y prueba en Chrome

Se repararon referencias documentales y de objetos, se sustituyeron los mapas
del atlas que disponían de equivalente español y se corrigió la búsqueda de
las seis escenas reflejadas para utilizar sus IDs, independientes del idioma.

La importación limpia se hizo con
`babele.syncImportedAdventureTokenNames = false`, evitando que Babele
sobrescribiera los nombres específicos de las fichas. No requirió reparación
posterior de nombres. Véase [IMPORTACION-LIMPIA.md](IMPORTACION-LIMPIA.md).

Después se corrigieron diez campos con cinco destinos del compendio retirado
`book` y 34 campos con 20 destinos de sección. Los encabezados españoles y las
páginas reubicadas se contrastaron con Foundry. Se actualizaron 39 campos del
mundo importado mediante sustituciones controladas, seguidas de otras 11.377
comprobaciones sin diferencias. Esta última prueba es una actualización del
mundo limpio, no una segunda importación desde cero. Los detalles y horas de
ejecución están en [VALIDACION-ENLACES-RUNTIME.md](VALIDACION-ENLACES-RUNTIME.md).

## Incidencias y alcance pendiente

1. **Texto incrustado en gráficos:** quedan rótulos ingleses en 14 fondos de
   escena y la escala del mapa de Puerto Nyanzaru para jugadores. Sustituir
   fondos por mapas del director puede revelar secretos o desajustar muros,
   rejillas y fichas. El inventario está en [REVISION-MAPAS.md](REVISION-MAPAS.md).
2. **Automatizaciones:** se han probado con éxito los casos documentados en
   [VALIDACION-AUTOMATIZACIONES.md](VALIDACION-AUTOMATIZACIONES.md), pero no el
   traslado efectivo de fichas por todos los teletransportes ni un
   restablecimiento completo de escenas. Tampoco se ha probado la navegación
   y las salvaciones de un grupo principal con guía, ni cada ataque o conjuro.
3. **Texto de macros originales:** la cobertura de las 126 claves de interfaz
   no certifica todos los mensajes ingleses incrustados en código del módulo
   original. Requieren una revisión específica de ejecución y localización.
4. **Diagnósticos de consola:** durante la sesión aparecieron mensajes del
   conversor `dnd5ePages` y de `TokenRing.getRingDataBySize`. Las comprobaciones
   documentales terminaron sin fallos; no se ha aislado la causa de esos
   mensajes y no se atribuyen a la traducción sin una reproducción comparada.
5. **Enlaces contextuales:** la resolución de los destinos absolutos no
   equivale a ejecutar todos los enlaces relativos en todos sus contextos.
   La auditoría conserva 1.142 referencias externas/contextuales como
   categoría separada, sin presentarlas como fallos confirmados.

## Continuación para una publicación final

Corregir los rótulos de los fondos conservando geometría y secretos; preparar
un grupo de prueba con guía y ejecutar los casos funcionales pendientes;
aislar los diagnósticos de consola y revisar los mensajes de las macros.
Después, repetir la importación desde cero con la versión candidata y
documentar los resultados antes de publicar.

Los cambios permanecen en commits locales de `develop`. Este trabajo no cambia
la versión del módulo ni publica una entrega.
