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

# Ejercicio 2: Tax_calculation

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

# Ejercicio 3: Add_student

Se requiere crear dos funciones que trabajen con una lista de estudiantes
y agreguen un nuevo estudiante a la lista. La diferencia es que la función
`add_student_by_value(list_students, new_student)` debe agregar al nuevo
estudiante usando paso por valor y la función
`add_student_by_reference(list_students, new_student)` usando paso por
referencia. Ambas funciones serán orquestadas desde la función
`main(list_students, new_student)` la cual ya está definida.

La función `add_student_by_value(list_students, new_student)` debe copiar
la lista de estudiantes para no afectar la lista original y agregar al nuevo
estudiante. Esta es la solución de paso por valor.

## Parámetros

- `list_students` (`List`): Lista de estudiantes original.
- `new_student` (`str`): Nombre del nuevo estudiante.

La función `add_student_by_reference(list_students, new_student)` debe agregar
al nuevo estudiante usando paso por referencia.

## Parámetros

- `list_students` (`List`): Lista de estudiantes original.
- `new_student` (`str`): Nombre del nuevo estudiante.

La función `main(list_students, new_student)` es la que llamará a las 2
funciones previamente definidas para comprobar que `list_students`
cambie de acuerdo a la función llamada.

## Parámetros

- `list_students` (`List`): Lista de estudiantes original.
- `new_student` (`str`): Nombre del nuevo estudiante.

## Ejemplo

### Entrada:
```python
list_students = ['Alice', 'Bob', 'Juan']
new_student_by_value = 'Maria'
new_student_by_reference = 'Sofia'

main(list_students, new_student_by_value, new_student_by_reference)
```
### Output:
```python
Original student list ['Alice', 'Bob', 'Juan']
Student list by value ['Alice', 'Bob', 'Juan', 'Maria']
Student list by reference ['Alice', 'Bob', 'Juan', 'Sofia']
Original student list ['Alice', 'Bob', 'Juan', 'Sofia']
```

[Ver ejercicio 3](03_add_student.py)

---

# Ejercicio 4: Sum_list_numbers

Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función `sum_list_numbers`, el parámetro debe ser nombrado correctamente, el
mismo debe recibir una lista.

Las buenas prácticas de programación de Python PEP8 las puedes encontrar en
el siguiente enlace:
https://peps.python.org/pep-0008/

La función debe retornar la suma de los números encontrados en la lista.

## Parámetro

El parámetro debe recibir la siguiente lista de números y debe ser nombrado
bajo las buenas prácticas de programación. Recibe la siguiente lista:

### Entrada:
```python
sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])
```
### Output
```python
339.35
10
```

[Ver ejercicio 4](04_sum_list_numbers.py)

---

# Ejercicio 5: Check_leap_year

Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función `check_leap_year`, el parámetro debe ser nombrado correctamente y
recibe como dato un año y mediante la función se debe retornar si este año es
bisiesto o no.

Para comprobar el año bisiesto fácilmente se puede utilizar la
operación mod `%`, el resultado de la operación del año a consultar `mod 4`
debe ser igual a `0` y además el año a consultar `mod 100` debe ser distinto de
`0`.

En el caso de obtener un resultado de `0` al realizar la operación del año
`mod 100` se debe comprobar adicionalmente que
el resultado del año a comprobar `mod 400` sea `0` para
considerar que sea un año bisiesto.

## Parámetros

- Año (`int`): El parámetro debe ser nombrado correctamente y recibe como dato un valor de tipo entero.

## Ejemplo

### Entrada:
```python
check_leap_year(2000)
```
### Output:
```python
True
```

[Ver ejercicio 5](05_check_leap_year.py)

---

# Ejercicio 6: Triangle_area_calculate

Implementa una función `triangle_area_calculate`, que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

## Parámetros

Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.

## Ejemplo

### Entrada:
```python
triangle_area_calculate(33, 45)
```
### Output:
```python
742.5
```

[Ver ejercicio 6](06_triangle_area_calculate.py)

---

# Ejercicio 7: Convert_to_integer

Implementa la función `convert_to_integer(string)` que reciba como parámetro
una cadena y retorne un número entero si es posible.
En caso contrario, debe retornar un mensaje indicando
que la cadena no puede ser convertida a un número entero o
un mensaje de error inesperado.
Para el error `ValueError` debe retornar `"The string cannot be converted to an integer"`;
si es cualquier otra excepción, debe
mostrar `"An unexpected error has occurred:"` seguido del error.

## Parámetros

- `string` (`str`): cadena que se desea convertir a un número entero.

## Ejemplo

### Entrada:
```python
convert_to_integer("123")
convert_to_integer("foo")
convert_to_integer(["3.14"])
```
### Output:
```python
123
The string cannot be converted to an integer
An unexpected error has occurred: int() argument must be a string, a bytes-like object or a number, not 'list'
```

[Ver ejercicio 7](07_convert_to_integer.py)

---

# Ejercicio 8: Get_element_from_list

Imagina que trabajas en una aplicación de gestión de inventarios. Para obtener
información sobre un producto, es necesario buscarlo en una lista. Sin embargo,
podría generarse un error si se ingresa un índice fuera del rango de la lista.
Así que debes manejar las excepciones.

Implementa `get_element_from_list(items_list, index)` que reciba una lista
y un índice, y retorne el elemento de la lista correspondiente al índice. Si
el índice está fuera del rango de la lista, la función debe retornar
`"The specified index is out of the list's range"`. En caso de un error inesperado, ha
de retornar `"An unexpected error has occurred: {error}"`.

## Parámetros

- `items_list` (`List`): Lista de la que se desea obtener el elemento.
- `index` (`int`): Índice del elemento que se desea obtener.

## Ejemplo

### Entrada:
```python
get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3)
get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5)
```
### Output:
```python
Notebook
Error: The specified index is out of the items_list range
```

[Ver ejercicio 8](08_get_element_from_list.py)

---

# Ejercicio 9: Calculate_factorial

Imagina que estás trabajando en una aplicación para calcular factoriales. Crea
una función `calculate_factorial(number)` que orquestará el proceso del cálculo
del factorial usando la función `factorial(number)` que recibirá un número entero
no negativo y calculará su factorial. Por lo tanto, debes manejar las excepciones
para controlar que las funciones se utilizan correctamente.

De esta manera, `calculate_factorial(number)` recibe un número entero y calcula su
factorial llamando a `factorial(number)`. Si ocurre una excepción al invocar a
`factorial(number)`, debe mostrar el mensaje de error:
`"An unexpected error has occurred: {error}"`.

## Parámetros

- `number` (`int`): El número del cual se desea calcular el factorial.

La función `factorial(number)` calcula el factorial del número. Si el número
introducido es negativo debe lanzar una excepción con el mensaje:
`"Factorial of a negative number cannot be calculated"`.

## Parámetros

- `number` (`int`): El número del cual se desea calcular el factorial.

## Ejemplo

### Entrada:
```python
calculate_factorial(5)
calculate_factorial(-5)
```
### Output:
```python
120
An unexpected error has occurred: Factorial of a negative number cannot be calculated...
```

[Ver ejercicio 9](09_calculate_factorial.py)