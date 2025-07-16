# sum_odd_numbers.py

def sum_odd_numbers(list_numbers: list) -> int:
    """ Función para sumar únicamente los números impares de una lista """

    # Variable vacía para sumar los numberos impares:
    total = 0

    for num in list_numbers:
        if type(num) != int or num < 0:
            raise ValueError("La lista debe contener solamente números enteros positivos!")

        # Calculamos si es impar
        elif num % 2 != 0:
            total += num

    return total


if __name__ == "__main__":
    print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))