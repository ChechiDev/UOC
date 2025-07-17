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
