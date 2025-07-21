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