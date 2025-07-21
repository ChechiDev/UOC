# convert_to_integer.py

import os

def convert_to_integer(string: str) -> None:
    """ Convierte una cadena de texto a int """

    # Intentamos convertir a int:
    try:
        return int(string)

    # Si falla porque la cadena no es convertible:
    except ValueError:
        return (f"Error: La cadena de texto '{string}' no puede convertirse a entero...")

    # Capturamos cualquiero otra excepción
    except Exception as e:
        return f"Error: Ha ocurrido un error -> {e}"


if __name__ == '__main__':
    os.system("cls")

    print(convert_to_integer("123"))
    print(convert_to_integer(["3.14"]))
    print(convert_to_integer("foo"))