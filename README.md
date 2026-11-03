# Arquitectura y BIM · Skills para empleados IA de IAbot.io

Planos, modelos, memorias y mediciones de arquitectura con referencias a la revisión del proyecto.

Procedimientos abiertos y concretos para agentes IA, con entradas, criterios de revisión y entregables. Publicados por [IAbot.io](https://iabot.io), plataforma de empleados IA con memoria, aplicaciones y ordenador virtual Linux.

## Habilidades y uso

| Skill | Empleado en IAbot.io | Entrega que revisar |
| --- | --- | --- |
| [Del plano acotado al modelo 3D](skills/architectural-plan-to-3d/SKILL.md) | un empleado de delineación y modelado | Modelo solicitado, editable, cotas de control y supuestos pendientes. |
| [Preparar y entregar renders Blender](skills/blender-pbr-render/SKILL.md) | un empleado de visualización arquitectónica | Imagen revisada, escena editable y relación de recursos utilizados. |
| [Diagnosticar materiales PBR](skills/pbr-material-render-review/SKILL.md) | un empleado de revisión de materiales | Informe estructural, diagnóstico visual y revisión corregida cuando esté autorizada. |
| [Redactar memorias de arquitectura](skills/architectural-report-writing/SKILL.md) | un empleado de documentación arquitectónica | Memoria editable, fuentes, anexos y lista de pendientes. |
| [Mediciones de obra trazables](skills/architectural-quantity-takeoff/SKILL.md) | un empleado de mediciones y presupuestos | Tabla editable de mediciones, subtotales y exclusiones. |
| [Coordinar planos, memoria y mediciones](skills/architectural-document-coordination/SKILL.md) | un empleado de coordinación documental de proyectos | Matriz de discrepancias con documentos afectados, impacto y decisión necesaria. |

## Instalación y uso en IAbot.io

```sh
npx skills add Iabot-io/architecture-skills --list
npx skills add Iabot-io/architecture-skills
```

En la plataforma, abre **Skills**, revisa la habilidad e impórtala con el ámbito adecuado. Adjunta sus entradas y da el encargo al empleado. Consulta [la guía de uso en IAbot.io](USO-EN-IABOT.md) para el recorrido completo.

## Ejemplos

- **Del plano acotado al modelo 3D:** «Convierte el plano adjunto en GLB conservando las cotas y huecos; identifica primero las alturas que faltan.»
- **Preparar y entregar renders Blender:** «Prepara esta escena para el render aprobado, conserva la cámara y entrega también el BLEND empaquetado.»
- **Diagnosticar materiales PBR:** «Averigua por qué el tapizado se ve liso; entrega las incidencias y una corrección comprobada.»

## Herramientas y límites

Necesita un visor de planos y herramientas de documentos; los trabajos 3D requieren CAD o Blender disponibles en el ordenador del empleado.

La colección no instala aplicaciones ni concede accesos. Las referencias se comprueban según la fecha, jurisdicción y alcance del encargo. Los resultados profesionales o administrativos conservan sus responsables y revisiones.

## Fuentes de referencia

- [Código Técnico de la Edificación](https://www.codigotecnico.org/)
- [Manual de Blender](https://docs.blender.org/manual/en/latest/)

Las fuentes orientan el método; su enlace no significa que una institución certifique o avale estas skills.

## Comprobación y licencia

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_skills.py
```

Se comprueban formato, recursos y referencias locales. Esa validación no acredita por sí sola un recorrido con un empleado real ni resultados en datos de producción. [Licencia MIT](LICENSE).

Agent Skills for AI employees and agents. Each skill includes an IAbot.io usage example and remains usable in compatible agents outside the platform.
