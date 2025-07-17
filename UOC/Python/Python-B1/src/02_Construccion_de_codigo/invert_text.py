# invert_text.py

def invert_text(text_chain: str) -> str:
    """ Función que invierte una cadena de texto """

    # Validamos la cadena de texto:
    if type(text_chain) != str:
        raise ValueError("El parámetro introducido debe ser una cadena de texto")

    # Devolvemos texto invertido:
    else:
        text_chain = text_chain.strip()
        return text_chain[::-1]


if __name__=="__main__":
    print(invert_text("Hello World!"))