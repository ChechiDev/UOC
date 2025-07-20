# is_palindrome.py

def is_palindrome(word: str) -> bool:
    """ Devuelve True si la palabra es un palíndromo usando recursividad """

    # Si la letra tiene 1 o menos letras, es palíndromo
    if len(word) <= 1:
        return True

    # Comparamos primer y ultimo carácter, si no coinciden no es palíndromo
    if word[0] != word[-1]:
        return False

    # Usamos recursivdad con la cadena restante sin el primer y ultimo carácter
    return is_palindrome(
        word[1:-1]
        )


if __name__ == "__main__":
    word = "level"
    print(f"Is '{word}' word palindrome?", is_palindrome(word))
    #
    word = "juan"
    print(f"Is '{word}' word palindrome?", is_palindrome(word))