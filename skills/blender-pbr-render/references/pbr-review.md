# Revisión de recursos y materiales

Separa cuatro preguntas: ¿la geometría es adecuada?, ¿el material está conectado?,
¿la iluminación permite verlo?, ¿el archivo de render conserva esas condiciones?

Un mapa base de color suele usar sRGB. Los mapas de datos, como rugosidad y normales,
deben interpretarse sin transformación de color. Un mapa de altura y una normal
RGB requieren nodos diferentes. Comprueba cada recurso en su función real.

Las normales tangentes necesitan una base UV coherente. Una imagen proyectada
con coordenadas de objeto no se convierte por sí sola en una normal tangente
válida. Examina costuras y deformaciones, además del nodo conectado.

Revisa textura a la distancia de entrega y en un acercamiento. La trama puede ser
físicamente correcta y ocupar menos de un píxel en la vista general; no alteres
su escala sin explicar el cambio. Reabrir el BLEND empaquetado permite comprobar
portabilidad; la inspección del PNG permite comprobar apariencia.

Referencias del fabricante:

- [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html).
- [Image Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/image.html).
- [Recursos empaquetados](https://docs.blender.org/manual/en/latest/files/blend/packed_data.html).
