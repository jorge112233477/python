def suma(*args):
    total = 0

    for n in args:
        total += n ** 2

    return total
    



def suma_absoluto(*args):
    total = 0

    for i in args:
        total += abs(i)

    return total
    



def numeros_persona(nombre,*args):
    
    suma_numeros = 0

    for i in args:
        suma_numeros += i

    return(f"{nombre}, la suma de tus números es {suma_numeros}")






