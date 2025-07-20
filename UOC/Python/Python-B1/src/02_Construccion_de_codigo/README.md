# Ejercicio 1: Fibonacci

Implementa la función `fibonacci(fibonacci_number)` que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado
`fibonacci_number` y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar
una excepción `ValueError("mensaje")`, la cual puede incluir un mensaje que debería
corresponder con el tipo de error durante la validación.

## Parámetros

- `fibonacci_number`: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

## Ejemplo

### Entrada:
```python
fibonacci(10)
```
### Output:
```python
55
```

[Ver ejercicio 1](01_fibonacci.py)

---

# Ejercicio 2: Sum_odd_numbers

Enunciado:
Crea una función `sum_odd_numbers(list_numbers)` que reciba como
parámetro una lista de números positivos enteros llamada `list_numbers`
y devuelva la suma de los números impares encontrados en la lista.
Considerar que `list_numbers` debe contener valores numéricos enteros mayores
o iguales a `0`, en caso contrario se debe mostrar un error tipo `ValueError`.

El error lo puedes mostrar con la siguiente instrucción:
`raise ValueError("MENSAJE DE ERROR")`

## Parámetros

- `list_numbers`: Lista de números enteros positivos.

## Ejemplo

### Entrada:
```python
sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])
```
### Output:
```python
30
```

[Ver ejercicio 2](02_sum_odd_numbers.py)

---

# Ejercicio 3: Invert_text

Implementa una función llamada `invert_text(text_chain)` que reciba como
parámetro una cadena de texto de tipo string llamada `text_chain` y devuelva
el texto invertido.

## Parámetros

- `text_chain`: Este parámetro solo admite strings.

## Ejemplo

### Entrada:
```python
invert_text('Hello world!')
```
### Output:
```python
!dlrow olleH
```

[Ver ejercicio 3](03_invert_text.py)

---

# Ejercicio 4: Count_vowels

Crea una función llamada `count_vowels(text_chain)` que reciba como parámetro
una cadena de texto de tipo string llamada `text_chain` y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha
cadena de texto.

## Parámetros

- `text_chain`: Este parámetro admite únicamente strings.

## Ejemplo

### Entrada:
```python
count_vowels('Hello world, this is an example.')
```
### Output:
```python
9
```

[Ver ejercicio 4](04_count_vowels.py)

---

# Ejercicio 5: Obtain_max

Implementar la función `obtain_max(list_numbers)` que recibe
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada `max`

## Parámetros

- `list_numbers`: Lista de números enteros

## Ejemplo

### Entrada:
```python
obtain_max([1, 45, 87, 21, 0, 23, 28])
```
### Output:
```python
87
```

[Ver ejercicio 5](05_obtain_max.py)

---

# Ejercicio 6: Calculate_angle

Utilizando la librería `math`, implementa una función llamada
`calculate_angle(angle)` que reciba como parámetro un número
correspondiente a un ángulo en grados llamado `angle` y retorne
como resultado el seno de dicho ángulo redondeado a 2 decimales.


## Parámetros

- `angle`: Entero correspondiente al valor de un ángulo.

## Ejemplo

### Entrada:
```python
calculate_angle(270)
```
### Output:
```python
-1
```

[Ver ejercicio 6](06_calculate_angle.py)

---

# Ejercicio 7: Line_graph

Enunciado:
Mediante la librería `matplotlib`, implementa una función llamada
`line_graph(x, y)`, se debe realizar únicamente la configuración
para la gráfica (sin mostrar nada en pantalla).
De esta forma, deberás configurar el título, que será `'Graph'`;
los labels de los ejes, que serán `'Axis X'` y `'Axis Y'` y activar
el grid.


## Parámetros

Los valores de los parámetros que recibe esta función son:

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
```
### Output:
```python
Matplotlib: Line Graph
```

[Ver ejercicio 7](07_line_graph.py)

---

# Ejercicio 8: Numpy_results

Implementar la función `numpy_results(list_numbers)` que reciba como parámetro una
lista que contiene números enteros y decimales llamada `list_numbers`, se pide
calcular el promedio y la desviación estándar mediante la
librería `Numpy` de todos los números dentro de la lista.

Cada resultado se debe imprimir en pantalla con su respectivo nombre
`Average: {value}` y `Standard deviation: {value}`, dichos resultados deben
estar redondeados a 2 decimales.

Los resultados también han de ser devueltos por la función.

Puedes consultar la referencia de la librería `Numpy` en el siguiente enlace:
https://numpy.org/doc/stable/reference/index.html#reference



## Parámetro

- `list_numbers`: Lista de números enteros y decimales.

## Ejemplo

### Entrada:
```python
[1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42]
```
### Output:
```python
Average: 19.74
Standard deviation: 26.03
```

[Ver ejercicio 8](08_numpy_results.py)

---

# Ejercicio 9

Implementa la función `mult_recursive(value, times)` que debe devolver el
resultado de sumar `value` `times` veces. Como puedes ver, su comportamiento
real es como si fuera una multiplicación. La función ha de ser implementada
usando recursividad. La función recibe dos parámetros:
- `value`: un número entero, que representa el número a sumar
- `times`: un número entero, que representa el número de veces que ha de sumarse `value` al resultado

Por ejemplo, si `value` vale 2 y `times` vale 3, la función ha de devolver 6, resultado sumar 2 + 2 + 2
Como puedes ver, su comportamiento real es como si fuera una multiplicación

## Parámetros

- `value`: número entero que se desea sumar
- `times`: número de veces que se desea sumar `value`

## Ejemplo

### Entrada:
```python
value = 2
times = 3
```
### Output:
```python
6
```

[Ver ejercicio 9](09_mult_recursive.py)

---

# Ejercicio 10

Enunciado:
Escribe una función llamada `invert_list(lst)` que reciba como parámetro
una lista `lst` y la invierta utilizando recursión. La función debe
devolver la lista invertida.

## Parámetros

- `lst` (`list`): una lista de elementos.

## Ejemplo

### Entrada:
```python
lst = [1, 2, 3, 4, 5]
print(invert_list(lst))
```
### Output:
```python
[5, 4, 3, 2, 1]
```

[Ver ejercicio 10](10_invert_list.py)