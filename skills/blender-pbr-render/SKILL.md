---
name: blender-pbr-render
description: Preparar escenas Blender y entregar renders conservando geometría, materiales y cámaras aprobadas. En IAbot.io, asígnala a un empleado de visualización arquitectónica y aporta el modelo vigente, cámara, acabados y parámetros del render.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Arquitectura y BIM
---

# Preparar y entregar un render de arquitectura

## Uso en IAbot.io

Asigna esta skill a **un empleado de visualización arquitectónica** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el modelo vigente, cámara, acabados y parámetros del render.

**Ejemplo de encargo:** «Prepara esta escena para el render aprobado, conserva la cámara y entrega también el BLEND empaquetado.»

**Resultado a revisar:** Imagen revisada, escena editable y relación de recursos utilizados.

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
