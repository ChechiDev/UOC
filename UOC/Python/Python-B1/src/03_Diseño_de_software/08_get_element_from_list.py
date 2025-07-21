# get_element_from_list.py


def get_element_from_list(items_list: list, index: int) -> str:
    """
    Devuelve el elemento de la lista en la posición indicada por el índice.
    Si el índice está fuera de rango, retorna un mensaje de error.
    Si ocurre cualquier otro error inesperado, retorna el mensaje de la excepción.
    """

    # Intentamos:
    try:
        return (items_list[index])

    except IndexError:
        return ("Error: The specified index is out of the items_list range")

    except Exception as e:
        return (f"Error: An unexpected error has ocurred: {e}")


if __name__ == '__main__':
    print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3))
    print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5))
