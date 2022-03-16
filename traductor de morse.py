diccionario = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "Ñ": "--.--",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": ".......",
}

#TRADUCTOR DE TEXTO A MORSE

def texto_morse(letra):
    if letra in diccionario:
        return diccionario[letra]
    else:
        return ""


def codificar(texto):
    texto = texto.upper()
    morse = ""

    for letra in texto:
        texto_traducido = texto_morse(letra)
        morse += texto_traducido + " "
    return morse


print("ingrese la frase para convertir a morse")
palabra = input()
codificado = codificar(palabra)
print("la frase en morse es: ", codificado)


# TRADUCTOR DE MORSE A TEXTO
def morse_texto(morse):
    for letra in diccionario:
        if diccionario[letra] == morse:
            return letra

    return ""


def decodificar(morse):
    texto = ""
    for letra_morse in morse.split(" "):
        letra = morse_texto(letra_morse)
        texto += letra
    return texto

print("ingrese el codigo morse para ser traducido")
palabra1 = input()
decodificado= decodificar(palabra1)
print("el texto traducido es: ", decodificado)