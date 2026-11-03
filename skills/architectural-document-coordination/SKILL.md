---
name: architectural-document-coordination
description: Detectar discrepancias entre planos, memorias, modelos y mediciones de una misma entrega. En IAbot.io, asígnala a un empleado de coordinación documental de proyectos y aporta el índice de planos, memoria, mediciones y revisiones vigentes.
license: MIT
metadata:
  author: IAbot.io
  version: 0.1.0
  sector: Arquitectura y BIM
---

# Coordinar planos, memoria y mediciones

## Uso en IAbot.io

Asigna esta skill a **un empleado de coordinación documental de proyectos** desde la biblioteca Skills de [IAbot.io](https://iabot.io). Aporta el índice de planos, memoria, mediciones y revisiones vigentes.

**Ejemplo de encargo:** «Comprueba esta entrega y registra contradicciones de superficies, materiales y revisiones sin corregirlas por tu cuenta.»

**Resultado a revisar:** Matriz de discrepancias con documentos afectados, impacto y decisión necesaria.

## Cuándo usarla y qué necesita

Detectar discrepancias entre planos, memorias, modelos y mediciones de una misma entrega

Trabaja con el índice de planos, memoria, mediciones y revisiones vigentes. Necesita un visor de planos y herramientas de documentos; los trabajos 3D requieren CAD o Blender disponibles en el ordenador del empleado.

## Procedimiento

1. Fija el conjunto de entrega y registra identificador, fecha, revisión y estado de cada documento; separa borradores y aprobados.
2. Relaciona plantas, estancias, elementos y partidas mediante identificadores compartidos, conservando los casos sin correspondencia.
3. Contrasta superficies, cotas de referencia, nombres y soluciones de acabado; anota ambos valores y la ubicación de cada evidencia.
4. Clasifica cada discrepancia por su efecto en geometría, coste, normativa o documentación; no elijas como correcta la versión más reciente por defecto.
5. Propón el responsable de resolución y qué documentos deberán revisarse juntos; conserva la incidencia hasta recibir una decisión trazable.

## Comprobación del resultado

- Todas las discrepancias enlazan al menos dos evidencias identificables.
- Las unidades y el tipo de superficie comparados son compatibles.
- Ningún documento aprobado se ha modificado durante la revisión.

## Entrega

Matriz de discrepancias con documentos afectados, impacto y decisión necesaria.

Conserva la identidad y revisión de las fuentes utilizadas. Señala los datos pendientes que afecten al resultado; no los sustituyas por valores inventados.

Usa [el registro de trabajo](assets/registro.csv) cuando no exista una plantilla del usuario; adapta sus filas sin perder las referencias.

## Referencias

- [Código Técnico de la Edificación](https://www.codigotecnico.org/)
- [Manual de Blender](https://docs.blender.org/manual/en/latest/)
