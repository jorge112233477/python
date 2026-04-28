
import random


print("JUEGO AHORCADO")

lista = ["muñeco", "Jorge", "pala", "cruz", "llave", "clase"]


def palabra_ale():
    return random.choice(lista)
    



def pedir_letra():
    return  input("Introduce una letra: ")



def ocultar_palabra(palabra):
    return ["_"] * len(palabra)



def chequear_letra(palabra, letra):
    return letra in palabra


def juego():
    palabra = palabra_ale()
    oculta = ocultar_palabra(palabra)

    while "_" in oculta:
        print(" ".join(oculta))
        
        letra = pedir_letra()

        if chequear_letra(palabra, letra):
            # actualizar palabra
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    oculta[i] = letra
        else:
            print("Fallaste")

    print("Ganaste:", palabra)


juego()



