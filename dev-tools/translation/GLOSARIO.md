# Glosario y criterios

La edición española aportada es la referencia de nombres propios del libro.
Las páginas siguientes son posiciones físicas en el PDF, empezando en 1.
El fichero `reviewed-segments.json` contiene equivalencias breves para aplicar
de manera uniforme. Incluye también traducciones editoriales de interfaz y
términos generales; no todas sus entradas son citas del libro.

| Inglés | Español | Referencia ES |
|---|---|---|
| Soulmonger | Almero | 6-8 |
| Death Curse | Maldición de muerte | 6-8 |
| Port Nyanzaru | Puerto Nyanzaru | 4, 16 |
| The Land of Chult | Las tierras de Chult | 4, 38 |
| Aldani Basin | Cuenca Aldani | 52 |
| Heart of Ubtao | Corazón de Ubtao | 50-52 |
| Firefinger | Dedo de Fuego | 7 |
| Fane of the Night Serpent | El Fano de la Serpiente Nocturna | 4 |
| Tomb of the Nine Gods | La Tumba de los Nueve Dioses | 4, 6 |
| Rotten Halls | Salones Putrefactos | 4 |
| Dungeon of Deception | Mazmorra de los Engaños | 4 |
| Vault of Reflection | Bóveda del Reflejo | 4 |
| Chambers of Horror | Cámaras del Horror | 4 |
| Gears of Hate | Engranajes del Odio | 4 |
| Cradle of the Death God | Cuna del Dios de la Muerte | 4 |
| Mantrap | Atrapahombres | 4 |
| Flail Snail | Caracol flagelo | 4 |
| Flying Monkey | Mono volador | 4 |
| Giant Snapping Turtle | Tortuga mordedora gigante | 4 |
| Thorny | Espinoso | 4 |
| Su-Monster | Sucarate | 4 |
| Harpers | Arpistas | 6 |
| Spellplague | Plaga de Conjuros | 6 |
| Red Wizards of Thay | Magos Rojos de Thay | 6 |
| archlich | archiliche | 6 |
| trickster gods | dioses embaucadores | 6 |
| Adventure Time | Hora de aventuras | 3 |
| Bag of Nails | Saco de Clavos | 5 |
| Flask of Wine | Jarro de Vino | 5 |
| I’jin | I’jin | 249, 251, 257; comprobación visual, no «Pjin» del OCR |
| River Mist | Bruma del Río | 5 |
| Grabstab | Pillapincha | 5 |
| Withers | Mustio | 5 |
| Salida | Salysa | 5 |
| Brazen Pegasus | Pegaso Fresco | 5 |
| Dragonfang | Colmillo de Dragón | 5 |
| Ring of Winter | Anillo del Invierno | 5 |
| Narwhal | Narval | 7 |
| Star Goddess | Diosa Estelar | 7 |
| Negative Plane | Plano Negativo | 7 |
| demiplane | semiplano | 7 |
| phylactery | filacteria | 7 |
| Thundering Lizard | Lagarto Atronador | 17 |
| Kaya’s House of Repose | Casa del Reposo de Kaya | 17 |
| Stormreach | Linde Tormentoso | 16 |
| Flaming Fist | Puño Ardiente | 31 |
| Lords’ Alliance | Alianza de los Lores | 31 |
| Ytepka Society | Sociedad Ytepka | 32 |
| Tinder | Yesca | 36 |
| Skullbash | Partecráneos | 36 |
| Weed | Hierbajo | 36 |
| Needle’s Bones | Huesos de Aguja | 35 |
| Summerwise | Estival | 18 |
| Hall of Gold | Pabellón de Oro | 24 |
| Grand Souk | Gran Zoco | 21 |
| Fort Nyanzaru | Fortín de Nyanzaru | 23 |
| Ortimay Swift and Dark | Ortimay Oscura y Veloz | 22 |
| Blue Mist Fever | Fiebre de la bruma azul | 41, con reglas distintas en Foundry |
| Shivering Sickness | Mal de los temblores | 41 |
| Throat Leeches | Sanguijuelas de la garganta | 41 |

«Fiebre de la bruma azul» corresponde a la versión inglesa de Foundry, que
reemplaza la «Fiebre del mono loco» del PDF por alucinaciones de monos azules
y salvaciones cada 24 horas. Se conserva esa diferencia mecánica. Para las
sanguijuelas se sigue el inglés: una salvación fallida aumenta el cansancio;
una exitosa lo reduce. El PDF español invierte ambas consecuencias.

En los contextos narrativos revisados, «Skullbash» es el nombre de la maza de
Musharib («Partecráneos»), y «Weed» es el apodo de Kupalue («Hierbajo»). Las
equivalencias antiguas de otros documentos no acreditan revisión contextual.

En `intro-02` se han comprobado visualmente las 48 filas de la página 5,
incluidas las pronunciaciones. «Salida» → «Salysa» se aplica como nombre propio
de ese PNJ; no debe reemplazar el sustantivo español «salida». Las equivalencias
de nombres aún deben comprobarse en las fichas y en el resto de los diarios.

Los términos añadidos durante el lote `intro-01` se han comprobado en ese
contexto; su inclusión aquí no implica que se hayan revisado todas sus
apariciones en el módulo. Se conserva «yuan-ti malison» en el resumen para
mantener la identificación de la criatura explícita en el original de Foundry.

## Criterios

Abreviaturas revisadas en `intro-03` (PDF ES, página física 7): pg = puntos de
golpe; CA = Clase de Armadura; CD = Clase de Dificultad; PX = puntos de experiencia;
ppt = platino; po = oro; pe = electro; pp = plata; pc = cobre; PNJ = personaje no
jugador. Alineamientos: LB, CB, NB, LN, N, CN, LM, CM y NM. Se traducen las siglas
visibles; las claves internas y las fórmulas de Foundry mantienen su sintaxis.

- Conservar el contenido mecánico de la edición de Foundry, incluso cuando
  difiera de las reglas impresas. No introducir conversiones numéricas de unidades.
- Mantener IDs, UUID, rutas de recursos, fórmulas, comandos de macros y scripts.
- Traducir etiquetas visibles de enlaces, conservando su destino.
- No sustituir imágenes oficiales. Los mapas y ayudas que llevan texto integrado
  en la imagen pueden seguir mostrando inglés aunque su nombre esté traducido.
- Preferir «conjuro», «tirada de salvación», «acción adicional» y «cansancio».
- Distinguir cobertura técnica, reutilización de otras traducciones y revisión
  lingüística contra el PDF. Una traducción automática no acredita esta última.
