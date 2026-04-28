def contar_primos(num):
    contadpr = 0

    for numero in range(2, num + 1):

        es_primo = True

        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break

        if es_primo:
            print(numero)
            contadpr += 1

    return contadpr


print(contar_primos(4))