# Referencias PDF para la traducción

Las dos ediciones locales se procesan con `prepare_pdf_references.py` y se
consultan en `data/references/`. Los PDF y el contenido extraído quedan excluidos
de Git mediante la regla existente `dev-tools/export/data/*`.

## Consulta

- `data/references/es/text.txt`: libro español, con separadores de página.
- `data/references/en/text.txt`: libro inglés, con separadores de página.
- `<idioma>/pages/0006.txt`: texto de una página concreta en UTF-8.
- `<idioma>/pages.jsonl`: una página por línea JSON, con texto y métricas.
- `<idioma>/pages/0006.native.txt`: extracción de la capa de texto original.
- `<idioma>/pages/0006.blocks.json`: bloques originales con coordenadas.
- `<idioma>/pages/0006.tsv.gz`: palabras, posiciones y confianza, solo con OCR.
- `<idioma>/bookmarks.json`: marcadores del PDF, si los hay.
- `<idioma>/manifest.json` y `manifest.json`: cobertura, errores, páginas para
  revisar, métodos, versiones y huellas SHA-256.

Desde la carpeta del módulo:

```powershell
rg -n -i 'Soulmonger|Almero' dev-tools/export/data/references/en/pages dev-tools/export/data/references/es/pages -g '*.txt' -g '!*.native.txt'
Get-Content dev-tools/export/data/references/es/pages/0006.txt -Encoding UTF8
```

Los números identifican páginas físicas del PDF, empezando en 1. No son
necesariamente los números impresos. La edición española tiene 259 páginas y
la inglesa 260: buscar correspondencias por título y contexto, sin asumir
equivalencia automática de páginas.

## Calidad y uso

Se conserva el flujo de texto del PDF para evitar mezclar líneas de columnas
contiguas. Se aplica OCR a páginas con menos de 80 caracteres o más de tres
caracteres alfabéticos ajenos al alfabeto latino, de sustitución o de uso privado.
Este criterio detecta problemas de codificación, pero no todos los errores.
Las páginas de pocas palabras o baja confianza aparecen en `review_pages`.
Estas pueden ser ilustraciones, mapas o páginas vacías.

La extracción es una referencia automática, no una transcripción revisada.
Puede omitir letras capitulares, separar palabras con guiones, confundir
símbolos y alterar tablas o el orden de lectura. La revisión visual de la
introducción confirma que el OCR recupera el encabezado español dañado, pero
omite la capitular inicial y confunde algunos símbolos de D&D. Contrastar
nombres, cifras, tablas y fragmentos dudosos con el PDF original.

Para traducir, localizar primero el pasaje inglés y después su equivalente
español. El libro español es la referencia de terminología; no sustituye la
estructura de Foundry. Conservar IDs, UUID, fórmulas, etiquetas y enlaces del
compendio al trasladar el texto. No distribuir estos archivos de referencia.

## Regeneración

Requiere Python, PyMuPDF, Tesseract y sus modelos `spa` y `eng`.
La instalación local de PyMuPDF está en `tmp/pdf-runtime`; los modelos están
en `tmp/tessdata`, y Tesseract en `C:/Program Files/Tesseract-OCR`.

```powershell
python -m pip install --target tmp/pdf-runtime pymupdf
python dev-tools/export/prepare_pdf_references.py
```

Se pueden indicar modelos alternativos con `--tessdata RUTA` y ajustar
`--workers 4`. El trabajo simultáneo se limita al OCR; el acceso a PyMuPDF
se serializa. El proceso reutiliza páginas cuya firma coincide con las fuentes,
las herramientas, los modelos y el script. El resultado solo está completo
cuando los dos manifiestos tienen `status: complete` y `errors: []`.
