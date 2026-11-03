---
name: architectural-quantity-takeoff
description: Produce traceable architectural quantity takeoffs from drawings or models, with explicit units, geometric formulas, opening deductions, revisions and reconciled totals by work item.
license: MIT
metadata:
  author: IAbot.io
  version: "0.1.0"
---

# Mediciones de arquitectura trazables

Úsala para obtener o revisar cantidades de obra. Necesita acceso a planos o modelos
y una herramienta de cálculo o tabla. Un presupuesto requiere además precios y
criterios económicos aportados o verificados para ese encargo.

## Definir la base

Identifica revisiones, unidades, partidas y alcance: existente, demolición, obra
nueva o acabados. Aclara el criterio de medición relevante antes de descontar
huecos o contar caras. Mantén diferenciadas cantidad geométrica, desperdicio,
coeficiente de compra y cantidad presupuestada.

## Medir y calcular

1. Organiza las filas por partida, planta y elemento. Usa
   [la plantilla CSV](assets/mediciones.csv) o el formato del usuario.
2. Conserva para cada fila la fuente, unidad, número de elementos, dimensiones y
   fórmula. Un dato sin fuente queda como pendiente y no entra como cero en un
   total que se presente como completo.
3. Convierte todas las dimensiones a la unidad de cálculo antes de operar. Para
   un paramento rectangular, por ejemplo, área bruta = número × longitud × altura;
   declara aparte los descuentos y comprueba que no produzcan áreas negativas.
4. Obtén huecos, encuentros, solapes y medición de ambas caras con el criterio
   acordado. No apliques un umbral universal de descuento.
5. Suma solo cantidades compatibles. Mantén m, m², m³, kg y unidades en grupos
   distintos. Evita contar un mismo elemento en una planta y en el total de conjunto.
6. Contrasta una muestra contra el plano o el modelo y reconcilia subtotales por
   planta con los totales por partida. Registra precisión y redondeo empleados.

## Entrega

Entrega la tabla editable con fórmulas o cálculo reproducible, el resumen por
partida y las exclusiones. Distingue medición cerrada de medición parcial. Si el
usuario solicita coste, añade fuente, fecha, moneda y alcance de los precios;
esta habilidad no proporciona precios vigentes ni impuestos por defecto.
