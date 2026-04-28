import random 

def lanzar_moneda():
    moneda = random.choice(["Cara", "Cruz"])
    return moneda

lista_numeros = [1,2,3,4,5,6,7]

def probar_suerte(resultado, lista):

    if resultado == "Cara":
        print("La lista se autodestruirá")
        return []
    
    elif resultado == "Cruz":
        print("La lista fue salvada")
        return lista

resultado = lanzar_moneda()
lista = probar_suerte(resultado, lista_numeros)

print(resultado)
print(lista)
