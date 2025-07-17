# 06_calculate_angle.py

import math as m

def calculate_angle(angle) -> int:
    """ Función que calcula el seno de un ángulo dado """

    # Verificamos parámetro:
    if type(angle) != int and type(angle) != float:
        raise ValueError("El ángulo debe ser un ángulo válido")

    else:
        # Convertimos los grados a radianes:
        radian_angle = m.radians(angle)

        # Calculamos el seno:
        result = m.sin(radian_angle)

    # Retornamos el seno del ángulo redondeado a 2 decimales:
    return round(result, 2)


if __name__=="__main__":
    print(calculate_angle(270))