# 04_count_vowels.py

def count_vowels(text_chain: str) -> int:
    """ Función que cuenta las vocales que hay en una cadena de texto """

    text_vowels = ["a", "e", "i", "o", "u"]
    total = 0

    # Validamos parámetro:
    if type(text_chain) != str:
        raise ValueError("El parámetro introducido debe ser una cadena de texto válida")

    else:
        # Convertimos a minúsculas:
        text_chain = text_chain.lower()

        # Contamos vocales:
        for i in text_chain:
            if i in text_vowels:
                total += 1

        return total


if __name__=="__main__":
    print(count_vowels("Hello world, this is an example."))