# fibonacci.py

def fibonacci(fibonacci_number: int) -> int:

    # Validamos los tipos de dato:
    if type(fibonacci_number) is str:
        raise ValueError(f"Error: El parámetro '{fibonacci_number}' no puede ser un texto")

    elif type(fibonacci_number) is float:
        raise ValueError(f"Error: El parámetro '{fibonacci_number}' no puede ser un decimal")

    elif fibonacci_number < 0:
        raise ValueError(f"Error: El parámetro '{fibonacci_number}' no puede ser un número negativo")

    elif fibonacci_number == 0:
        return 0

    elif fibonacci_number == 1:
        return 1

    n1 = 0
    n2 = 1

    # Calculamos el número de Fibonacci iterativamente actualizando los valores de n1 y n2
    for i in range(2, fibonacci_number + 1):
        temp_num = n2
        n2 = n1 + n2

        n1 = temp_num

    return n2

# Comprobamos
if __name__ == "__main__":
    print(fibonacci(10))