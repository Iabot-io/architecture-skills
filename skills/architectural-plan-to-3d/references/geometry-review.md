# Comprobación de geometría y exportación

Registra las comprobaciones que corresponden al alcance del encargo:

| Control | Fuente | Editable | Archivo exportado |
| --- | --- | --- | --- |
| Unidades y escala | Unidad declarada y cotas elegidas | Unidad de escena y factor de importación | Unidad interpretada al reabrir |
| Dimensiones globales | Anchura, longitud y alturas conocidas | Distancias medidas | Distancias medidas |
| Muros y huecos | Extremos, espesores, anchuras y posiciones | Geometría y vacíos | Geometría y vacíos |
| Plantas | Nombre y cota conocida | Organización e identificadores | Componentes presentes |
| Exclusiones | Lista solicitada | Selección de exportación | Ausencia comprobada |

Una tolerancia depende del uso y de la precisión de la fuente. Declárala con sus
unidades antes de juzgar la desviación; no uses un porcentaje universal. En una
imagen escaneada, distingue error de lectura, deformación del escaneo y error de
modelado. Si dos cotas contradicen la escala, conserva la incidencia sin corregir
una medida arbitrariamente.

Para GLB, la [especificación glTF](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
define metros como unidad de distancia. Comprueba el factor aplicado en la
exportación desde el CAD y vuelve a medir. La visualización del modelo no
determina por sí sola la unidad original del plano.
