# check_age.py

def check_age(age: int) -> int:
    """ Retorna True si la edad del parámetro es mayor o igual a 18 """

    return age >= 18


if __name__ == "__main__":
    print(check_age(15))
    print(check_age(17))
    print(check_age(18))