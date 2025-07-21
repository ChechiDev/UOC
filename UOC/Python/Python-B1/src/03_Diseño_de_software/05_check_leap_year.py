# check_leap_year.py

def check_leap_year(year: int) -> bool:
    """ Comprueba si un año es bisiesto """

    # Si el año es divisible por 4 y no por 100, o si es divisible por 400 -> es bisiesto
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False


if __name__ == '__main__':
    year = 2000
    print(check_leap_year(year))