# invert_list.py

def invert_list(lst: list) -> list:
    """ Invierte una lista usando recursividad """

    # Validamos:
    if len(lst) <= 1:
        # Retornamos el mismo elemento:
        return lst

    # Usamos recursividad para invertir la lista.
    # Cogemos el último elemento de la lista y lo colocamos la principio:
    return [lst[-1]] + invert_list(lst[:-1])


if __name__=="__main__":
    lst = [1, 20, 3, 40, 5]
    print(invert_list(lst))