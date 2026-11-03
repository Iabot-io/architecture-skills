---
name: blender-pbr-render
description: Prepare existing Blender architectural scenes for rendering, preserving approved geometry, camera and PBR assets, then verify the requested image and editable handoff.
license: MIT
metadata:
  author: IAbot.io
  version: "0.1.0"
---

# Preparar y entregar un render de arquitectura

Necesita Blender y la vía de render autorizada para el encargo. Si el usuario
entrega un modelo existente, úsalo como fuente; no reconstruyas el edificio para
modificar materiales o presentación.

## Escena y decisiones vigentes

Abre la revisión actual e identifica resultado, cámara, alcance, resolución y
decisiones ya aprobadas. Conserva geometría, distribución y mobiliario que no
estén incluidos en el cambio. Guarda una revisión editable antes de intervenir.

Comprueba los recursos disponibles y sus licencias antes de elegir materiales o
muebles. Un enlace de catálogo no demuestra que el archivo exista localmente.
Para cambios de acabado, conserva textura, relieve y escala física; un color
uniforme no sustituye un material textil solicitado.

## Preparación

1. Verifica la cámara activa y su encuadre sobre la escena real. Mantén focal,
   posición y orientación aprobadas; declara las decisiones de presentación nuevas.
2. Revisa unidades, apoyos, intersecciones visibles y superficies sin material.
   Separa defectos geométricos de los de iluminación o sombreado.
3. Registra procedencia, licencia y tamaño físico de cada textura nueva. Configura
   el espacio de color según el uso del mapa y comprueba normales y UV.
4. Guarda el BLEND con la cámara y los cambios. Empaqueta recursos necesarios,
   convierte en locales las dependencias permitidas y reabre la copia preparada.
5. Revisa una vista actual de la escena. Si se pide captura de la aplicación,
   entrega una captura real del visor; identifica por su nombre cualquier render
   de previsualización. Respeta el punto de aprobación acordado, si existe.

## Render y revisión

Reutiliza la herramienta local o remota que el usuario haya autorizado. Respeta
las restricciones de GPU, coste y resolución de ese entorno; esta skill no fija
un proveedor ni concede presupuesto. En un servicio asíncrono, conserva el
identificador del trabajo y consulta su estado antes de considerar otro envío.

Abre la imagen terminada. Comprueba encuadre, aspecto de materiales, recursos
ausentes, ruido, transparencia y resolución. El estado «completado» solo acredita
que terminó el proceso. Si hay un defecto, corrige su causa y verifica el cambio
antes de generar otra variante.

Entrega el render solicitado y la revisión editable correspondiente, con los
supuestos y limitaciones relevantes. Para diagnosticar telas lisas o normales
incoherentes, usa [la guía de PBR](references/pbr-review.md).
