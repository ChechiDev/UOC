# triangle_area_calculate.py

import os

def triangle_area_calculate(base, height):
    """ Calcula y devuelve el área de un triángulo usando base y altura """

    # Comprobamos si los params son positivos:
    if base <= 0 or height <= 0:
        raise ValueError("La base y la altura deben ser números positivos...")

    # Calculamos:
    return (base * height) / 2


if __name__ == '__main__':
    print(triangle_area_calculate(33, 45))