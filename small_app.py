while True:
    try:
        nombre = str(input("Introduce tu nombre: "))
        edad = int(input("Introduce tu edad: "))
        break
    except:
        print("Eso no es valido, intentelo otra vez")


edad_futura = edad + 10

print(f"Hola {nombre}, tu edad dentro de 10 años sera {edad_futura}")