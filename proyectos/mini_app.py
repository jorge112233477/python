


edades = []


try:
    with open("edades.txt", "r") as archivo:
        for linea in archivo:
            edades.append(int(linea.strip()))
except:
    pass


def guardar_edad(lista, edad):
    lista.append(edad)


    with open("edades.txt", "a") as archivo:
        archivo.write(str(edad) + "\n")



def calcular_edad(edad):
    return edad + 10
    

def suma_numeros(a,b):
    return a + b



def saludar():
    nombre = input("Dime tu nombre: ")
    print(f"Hola {nombre} encantado de conocerte.")
    
    


    






while True:
    print("\n ---Menu---")
    print("1. Saludar")
    print("2. Calcular edad futura")
    print("3. sumar numeros")
    print("4. guardar edad")
    print("5. ver edad")
    print("6. Salir")

    opcion = input("Introduce una opcion: ")

    if opcion == "1":
        saludar()
    
    
    elif opcion == "2":
        while True:
            try:
                edad = int(input("Dime tu edad:  "))
                break
            except:
                print("No valido, intentelo de nuevo")

        resultado = calcular_edad(edad)
        print(f"En 10 años tendras {resultado}")




    elif opcion == "3":
        while True:
            try:
                numero1 = int(input("Eliga el primer numero: "))
                numero2 = int(input("Eliga el segundo numero: "))
                break
            except:
                print("No valido. intentelo de nuevo")
                
        resultado_suma = suma_numeros(numero1, numero2)
        print(f"la suma de tus dos numeros es {resultado_suma}")


    
    elif opcion == "4":
        while  True:
            try:
                edad = int(input("Introduzca su edad: "))
                guardar_edad(edades, edad)
                break

            except:
                print("No valido. eliga otra edad") 

        print("La edad se guardo correctamente")



    elif opcion == "5":
        if len(edades) == 0:
            print("No hay edades guardadas")
        
        else:
            print("Edades guardadas: ")
            for edad in edades:
                print(f"- {edad} ")

        


    

    
    elif opcion == "6":
        print("saliendo....")
        break


    else:
        print("Opcion no valida, eliga una disponible")










    







