# 05_obtain_max.py

def obtain_max(list_numbers: list) -> int:
    """ Función que obtiene el número máximo de una lista de números """

    # Validamos parámetro:
    if type(list_numbers) != list:
        raise ValueError("El parámetro introducido tiene que ser una lista de números válida")

    return max(list_numbers)


if __name__=="__main__":
    print(obtain_max([1, 45, 87, 21, 0, 23, 28]))