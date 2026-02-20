from langdetect import detect, LangDetectException
import string

ALFABETO = string.ascii_lowercase + "0123456789"

def algoritmo_de_cifrado(texto_cifrado, clave_decifrado, direccion):
    """Descifra el texto cifrado a partir de una clave de descifrado"""

    texto_plano = ""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra
        else:
            indice_letra_cifrada = ALFABETO.index(letra)

            if direccion == "izquierda":
                indice_letra_descifrada = (indice_letra_cifrada - clave_decifrado) % len(ALFABETO)
            else:  
                indice_letra_descifrada = (indice_letra_cifrada + clave_decifrado) % len(ALFABETO)

            texto_plano += ALFABETO[indice_letra_descifrada]

    return texto_plano


def FuerzaBruta(texto_cifrado):
    espacio_claves = range(len(ALFABETO))


    print("\n--- Recorrido hacia la IZQUIERDA ---\n")
    for clave in espacio_claves:
        texto_plano = algoritmo_de_cifrado(texto_cifrado, clave, "izquierda")
        try:
            if detect(texto_plano) == 'es':
                print(f"[IZQUIERDA] Clave: {clave}")
                print(f"Texto: {texto_plano}\n")
        except LangDetectException:
            continue


    print("\n--- Recorrido hacia la DERECHA ---\n")
    for clave in espacio_claves:
        texto_plano = algoritmo_de_cifrado(texto_cifrado, clave, "derecha")
        try:
            if detect(texto_plano) == 'es':
                print(f"[DERECHA] Clave: {clave}")
                print(f"Texto: {texto_plano}\n")
        except LangDetectException:
            continue


if __name__ == "__main__":
    texto_cifrado = input("Por favor introduce el texto cifrado: ").lower()
    FuerzaBruta(texto_cifrado)