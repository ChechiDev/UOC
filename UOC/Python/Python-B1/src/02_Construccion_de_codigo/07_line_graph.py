# 07_line_graph.py
# Doc matplotlib: https://matplotlib.org/stable/users/index

import matplotlib.pyplot as plt


def line_graph(x: list, y: list) -> None:
    """ Dibuja un gráfico de líneas usando listas x, y """

    # Validamos params:
    if type(x) != list and type(y) != list:
        raise ValueError("Los parámetros deben ser una lista de números válida")

    else:
        # Configuramos el titulo del graph:
        plt.title("Line Graph")

        # Configuramos las etiquetas x, y:
        plt.xlabel("Axis-X")
        plt.ylabel("Axis-Y")

        # Activamos grid:
        plt.grid(True)

        # Ploteamos:
        plt.plot(x, y)
        plt.show()


if __name__=="__main__":
    line_graph([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])