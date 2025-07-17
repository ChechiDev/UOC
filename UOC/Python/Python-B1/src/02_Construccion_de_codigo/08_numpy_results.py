# 08_numpy_results.py

import numpy as np

def numpy_results(list_numbers):
    """ Devuelve estadísticas básicas de una lista usando numpy """

    # Validamos lista:
    if type(list_numbers) != list:
        raise ValueError("El parámetro introducido debe ser una lista válida")

    # Calculamos promedio (la media de la lista):
    avg = (
        round(np.mean(list_numbers), 2)
    )

    # Calculamos la desviación estándar:
    std_desv = (
        round(np.std(list_numbers), 2)
    )

    # Imprimimos resultado:
    print(f"Average: {avg}")
    print(f"Standard deviation: {std_desv}")

    return avg, std_desv


if __name__=="__main__":
    numpy_results([1, 2, 10, -5, 0, 9.55, 74.825, 55, 8, 42])