---
name: pbr-material-render-review
description: Diagnosticar texturas, UV, normales y empaquetado antes de repetir un render. En IAbot.io, asígnala a un empleado de revisión de materiales y aporta el BLEND y la imagen que muestra el defecto.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Arquitectura y BIM
---

# Diagnóstico de materiales PBR

## Uso en IAbot.io

Asigna esta skill a **un empleado de revisión de materiales** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el BLEND y la imagen que muestra el defecto.

**Ejemplo de encargo:** «Averigua por qué el tapizado se ve liso; entrega las incidencias y una corrección comprobada.»

**Resultado a revisar:** Informe estructural, diagnóstico visual y revisión corregida cuando esté autorizada.

## Inventario estructural

Ejecuta el ayudante incluido con las opciones de seguridad de Blender:

```sh
blender --background --disable-autoexec escena.blend --python scripts/audit_materials.py -- --out materiales.json --require-texture Tapizado
```

Repite `--require-texture` para cada material que deba usar imágenes. Omítelo para
obtener el inventario general. La ruta del script es relativa a esta carpeta.
El código 2 indica incidencias; el script lee la escena y no renderiza ni guarda
cambios en el BLEND. Ejecuta únicamente archivos de un origen autorizado.

El informe detecta determinadas pérdidas de conectividad y portabilidad.
`visual_review_required` permanece verdadero: ni `structural_ok` ni la existencia
de imágenes certifican realismo, escala física, calidad o todos los nodos internos
de un grupo. Revisa manualmente los grupos señalados y las superficies visibles.

## Diagnóstico dirigido

- Confirma que las caras visibles utilizan el material esperado y que su salida
  activa recibe los nodos de imagen. Una etiqueta del material no prueba apariencia.
- Separa textura ausente, mapa mal conectado, coordenadas incorrectas y mala
  iluminación. Conserva cámara y geometría cuando no causen el defecto.
- Registra tamaño físico y unidades del recurso. Inspecciona el acabado a distancia
  de entrega y de cerca antes de cambiar escala o número de muestras.
- Usa mapas de datos sin transformación de color. Comprueba que la base UV de
  una normal tangente coincide con la utilizada por su imagen; revisa costuras.
- Empaqueta, guarda y reabre después de corregir recursos. Conserva la licencia y
  procedencia de las imágenes que se incorporen al proyecto.

## Evidencia final

Renderiza por la vía autorizada solo cuando el encargo incluya esa comprobación.
Inspecciona el resultado real y explica qué defecto se corrigió. Entrega informe,
imagen de comparación cuando exista y revisión editable. Si no hubo render nuevo,
indica que se comprobó la estructura y conserva pendiente la apariencia final.

Fuentes: [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html)
y [recursos empaquetados](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html).
