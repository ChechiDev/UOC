# tax_caculation.py


def tax_calculation_global(value: int) -> float:
    """ Calcula el impuesto global (19%) para un valor dado """

    # Configuramos los impuestos al 19%:
    tax_percent = 19

    return (
        (tax_percent * value) / 100
    )



def tax_calculation_group_1(value: int) -> float:
    """ Calcula el impuesto del grupo 1 (24%) para un valor dado """

    # Configuramos los impuestos al 24%:
    tax_percent = 24

    return (
        (tax_percent * value) / 100
    )


if __name__ == "__main__":
    print(f"The taxes for group global: {tax_calculation_global(500)}")
    print(f"The taxes for group 1: {tax_calculation_group_1(500)}")