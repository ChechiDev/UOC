# sum_list_numbers.py

import os

def sum_list_numbers(
        list_numbers: list
) -> None:
    """ Devuelve la suma de los números de una lista """

    # Calculamos la suma de los números:
    return sum(
        list_numbers
    )


if __name__ == '__main__':
    os.system("cls")

    print(sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]))
    print(sum_list_numbers([1, 2, 3, 4]))
