# Architecture skills · IAbot.io

**Habilidades abiertas para agentes de IA que preparan planos, modelos 3D,
renders y documentación de arquitectura.**

Publicadas por [IAbot.io](https://iabot.io), plataforma de empleados de inteligencia
artificial. Cada habilidad define un trabajo concreto, sus evidencias y su entrega.
Usan el formato abierto [Agent Skills](https://agentskills.io/specification).

## Habilidades

| Skill | Trabajo y entregable |
| --- | --- |
| [architectural-plan-to-3d](skills/architectural-plan-to-3d/SKILL.md) | Convertir un plano acotado en geometría comprobada y exportar un modelo 3D con sus supuestos documentados. |
| [blender-pbr-render](skills/blender-pbr-render/SKILL.md) | Preparar cámara, materiales y recursos de una escena Blender; entregar el render solicitado y su editable. |
| [pbr-material-render-review](skills/pbr-material-render-review/SKILL.md) | Diagnosticar texturas, UV y normales; generar un informe estructural y revisar el aspecto real. |
| [architectural-report-writing](skills/architectural-report-writing/SKILL.md) | Redactar una memoria con datos trazables, anexos y pendientes explícitos. |
| [architectural-quantity-takeoff](skills/architectural-quantity-takeoff/SKILL.md) | Preparar mediciones por partida, planta y fuente, con unidades y reglas de descuento declaradas. |

## Instalación

```sh
# Explorar sin instalar
npx skills add iabot-io/architecture-skills --list

# Elegir habilidades y agente de destino
npx skills add iabot-io/architecture-skills

# Instalar una habilidad concreta
npx skills add iabot-io/architecture-skills --skill architectural-report-writing
```

El CLI y [skills.sh](https://skills.sh) son proyectos externos. Las instalaciones
con telemetría habilitada contribuyen al descubrimiento según sus reglas;
publicar una colección no garantiza posición ni plazo de indexación.

## Uso

Ejemplos de encargos:

- «Convierte este plano acotado en GLB. Conserva huecos y unidades; enumera las
  cotas que faltan antes de modelar lo que dependa de ellas».
- «Revisa por qué la tela se ve lisa en este BLEND y este render. Conserva la
  cámara y la geometría aprobadas».
- «Prepara la memoria descriptiva de esta reforma con estos documentos. Marca
  los datos ausentes y referencia de dónde sale cada superficie».

Las skills de documentación funcionan con las herramientas habituales de archivos
del agente. Las de 3D necesitan las aplicaciones indicadas en su `SKILL.md`.
Instalar instrucciones no instala Blender ni concede acceso a una GPU. Los scripts
se ejecutan solo cuando el trabajo los requiere. Los criterios normativos se
comprueban con fuentes vigentes de la jurisdicción del proyecto.

## Validación y aportaciones

```sh
python3 -m pip install -r scripts/requirements-validation.txt
python3 scripts/validate_skills.py
```

Para proponer una mejora, aporta un caso anonimizado, el resultado esperado y
la comprobación que permite revisarlo. Conserva las fuentes de recursos ajenos y
sus licencias. Los ejemplos deben distinguir medidas conocidas de estimaciones.

## English

Open architecture skills for AI agents: dimensioned plans to 3D, Blender scene
preparation, PBR material review, technical reports and traceable quantity takeoff.
Instructions are in Spanish; skill names and descriptions support discovery in
English. Follow the user's language for deliverables. Published under the
[MIT license](LICENSE) by [IAbot.io](https://iabot.io).
