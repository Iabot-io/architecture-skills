---
name: architectural-plan-to-3d
description: Convertir planos acotados en geometría 2D comprobada y un modelo 3D editable. En IAbot.io, asígnala a un empleado de delineación y modelado y aporta el plano, su revisión, unidades y cotas conocidas.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Arquitectura y BIM
---

# Del plano de arquitectura al modelo 3D

## Uso en IAbot.io

Asigna esta skill a **un empleado de delineación y modelado** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el plano, su revisión, unidades y cotas conocidas.

**Ejemplo de encargo:** «Convierte el plano adjunto en GLB conservando las cotas y huecos; identifica primero las alturas que faltan.»

**Resultado a revisar:** Modelo solicitado, editable, cotas de control y supuestos pendientes.

## Identificar la fuente y la escala

- Abre el archivo y la revisión exactos del encargo. Identifica planta, unidades,
  cotas legibles, perímetro, particiones, huecos y orientación. Un nombre de archivo
  no acredita su contenido.
- En un plano raster, calibra con una cota fiable. Registra la cota elegida y la
  transformación entre píxeles y unidades; comprueba otra cota independiente cuando
  esté disponible. Si falta escala, prepara el inventario de datos pendientes.
- Separa hechos observados, datos aportados y estimaciones aceptadas. Pregunta por
  las alturas que bloqueen la extrusión; no conviertas alturas típicas en medidas
  del proyecto.

## Construir geometría comprobable

1. Conserva el original y trabaja en una revisión nueva del editable.
2. Traza primero el plano 2D. Interpreta capas, bloques, tramas, cotas y leyendas
   conjuntamente; una trama o el símbolo de un mueble no define por sí solo un muro.
3. Compara el trazado con el original mediante superposición o vistas equivalentes.
   Revisa perímetro, huecos, espesor y extremos antes de extruir.
4. Construye el 3D desde esa geometría. Conserva posiciones, rotaciones y unidades
   de los bloques confirmados. Mantén identificables plantas y componentes.
5. Si se autoriza una propuesta con supuestos, registra cuáles son y etiqueta el
   modelo como propuesta. Conserva separada la geometría medida.

## Exportar y entregar

Reabre el archivo exportado con un visor o parser compatible. Revisa su unidad,
dimensión global, cotas de control, huecos y componentes incluidos. Verifica las
exclusiones en el exportado: ocultar un objeto en el visor no acredita su exclusión.
Usa [la revisión geométrica](references/geometry-review.md) al comprobar conversiones
de formato o escala.

Entrega el formato solicitado, el editable si se pidió y un resumen de la fuente,
revisión, unidades, comprobaciones y pendientes. Una captura o un render acompaña
al modelo, pero no sustituye el archivo 3D pedido. La revisión visual no certifica
un proyecto para construcción.
