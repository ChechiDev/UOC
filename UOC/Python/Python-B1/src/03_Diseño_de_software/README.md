# Tema-3: Diseño de software

# Ejercicio 1: Sum_even_numbers_in_list

Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones `sum_even_numbers_in_list_while(list_numbers)`,
`sum_even_numbers_in_list_for(list_numbers)` y
`sum_even_numbers_in_list_do_while(list_numbers)` en donde su parámetro
sea una lista de números y utilice un bucle `WHILE`, `FOR` y `DO WHILE`, respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

## Parámetros

- `list_numbers` (`List`): lista de precios que se desea sumar

## Ejemplo

### Entrada:
```python
shopping_list = [10, 449, 33, 44, 188, 640]
sum_even_numbers_in_list_while(shopping_list)
sum_even_numbers_in_list_for(shopping_list)
sum_even_numbers_in_list_do_while(shopping_list)
```
### Output:
```python
En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640.
```

[Ver ejercicio 1](01_sum_even_nums_in_list.py)

---

# Ejercicio 2

Implementa la función `tax_calculation_global(value)` que calcula los impuestos
a pagar de un valor numérico dado.
Implementa también la función `tax_calculation_group_1(value)`, que calcula los
impuestos para un grupo de productos diferente que tiene un porcentaje menor.

La función `tax_calculation_global(value)` calcula el valor de impuestos usando
el valor de porcentaje (`tax_percent`) de 24. De esta manera, calcularía los impuestos
mediante la siguiente fórmula: (`tax_percent` * `value`) / 100

## Parámetros

- `value`: un número entero, que representa el valor al cual se le calcularán
los impuestos.

La función `tax_calculation_group_1(value)` calcula los impuestos para el grupo 1 de
productos, que tiene un valor de porcentaje (`tax_percent`) de 19.

## Parámetros

- `value`: un número entero, que representa el valor al cual se le calcularán
los impuestos.

Por ejemplo, si se llama a las funciones con un valor de 500, la función
`tax_calculation_global(500)` calcula el valor del impuesto global que tiene un porcentaje
del 24%, y la función `tax_calculation_group_1(500)` calcula el valor del impuesto para el
grupo 1, que son el 19% del valor.

### Entrada:
```python
tax_calculation_global(500)
tax_calculation_group_1(500)
```
### Output:
```python
120.0
95.0
```

[Ver ejercicio 2](02_tax_calculation.py)

---
