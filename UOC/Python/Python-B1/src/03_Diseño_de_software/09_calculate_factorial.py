# calculate_factorial.py


def factorial(number: int) -> int:
    """
    Calcula el factorial de un número entero de forma recursiva.
    Lanza ValueError si el número es negativo.
    """
    # Comprobamos:
    if number < 0:
        raise ValueError("Factorial of a negative number cannot be calculated...")

    elif number == 0:
        return 1
    # Multiplicamos el número actual por el factorial del número anterior (recursivamente)
    return number * factorial(number - 1)


def calculate_factorial(number: int) -> int:
    """
    Devuelve el factorial de un número usando la función factorial.
    Si ocurre un error, retorna el mensaje de la excepción.
    """
    # Intentamos devolver el factorial:
    try:
        return factorial(number)

    except Exception as e:
        return f"An unexpected error has occurred: {e}"


if __name__ == '__main__':
    print(calculate_factorial(5))
    print(calculate_factorial(-5))