# find_max.py

def find_max(lst):
    """ Devuelve el valor máximo de una lista usando recursividad """
    # Si la lista solo contiene 1 valor, lo devolvemos:
    if len(lst) == 1:
        return lst[0]

    # Aplicamos recursividad:
    else:
        max_value = find_max(lst[1:]) # Llamada recursiva con el resto de la lista
        if lst[0] > max_value:
            return lst[0]

        return max_value


if __name__ == "__main__":
    numbers_list = [1, 5, 2, 7, 3]
    print(find_max(numbers_list))
