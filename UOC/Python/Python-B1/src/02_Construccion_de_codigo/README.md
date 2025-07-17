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
### Salida:
```python
55
```

[Ver ejercicio 1](fibonacci.py)

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
### Salida
```python
30
```

[Ver ejercicio 2](sum_odd_numbers.py)

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

### Salida:
```python
!dlrow olleH
```

[Ver ejercicio 3](invert_text.py)