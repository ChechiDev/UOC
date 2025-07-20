# 09_mult_recursive.py

def mult_recursive(value: int, times: int) -> int:
    """ Suma un valor dado por las veces dadas, usando recursividad """

    # Comprobamos parámetros:
    if not (type(value) == int and type(times) == int):
        raise ValueError("Los parámetros introducidos deben ser números enteros")

    # En el caso de que times sea 0:
    if times == 0:
        return 0

    # Aplicamos recursividad
    else:
        return value + mult_recursive(value, times -1)


if __name__=="__main__":
    print("Must print 6: ", mult_recursive(2, 3))