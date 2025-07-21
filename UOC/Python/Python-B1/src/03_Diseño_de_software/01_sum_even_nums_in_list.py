# sum_even_nums_in_list.py

import os

# Suma con While:
def sum_even_numbers_in_list_while(list_numbers: list) -> int:
    i = 0
    suma = 0

    while i < len(list_numbers):
        if list_numbers[i] % 2 == 0: # Si el num es par, lo sumamos
            suma += list_numbers[i]

        i += 1

    return suma


# Suma con For:
def sum_even_numbers_in_list_for(list_numbers: list) -> int:
    suma = 0

    for num in list_numbers:
        if num % 2 == 0:
            suma += num

    return suma


# Suma con DO While:
def sum_even_numbers_in_list_do_while(list_numbers: list) -> int:
    i = 0
    suma = 0

    while True:
        if list_numbers[i] % 2 == 0:
            suma += list_numbers[i]

        i += 1

        if i >= len(list_numbers):
            break

    return suma


if __name__ == "__main__":
    os.system("cls")
    shopping_list = [10, 449, 33, 44, 188, 640]
    print(sum_even_numbers_in_list_while(shopping_list))
    print(sum_even_numbers_in_list_for(shopping_list))
    print(sum_even_numbers_in_list_do_while(shopping_list))
