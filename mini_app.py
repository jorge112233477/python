

while True:
    print("\n ---Menu---")
    print("1. Saludar")
    print("2. Calcular edad futura")
    print("3. Salir")

    opcion = input("Introduce una opcion: ")

    if opcion == "1":
        nombre = input("Dime tu nombre: ")
        print(f"Hola {nombre} encantado de conocerte.")

    
    elif opcion == "2":
        while True:
            try:
                 edad_actual = int(input("dime tu edad: "))
                 break
            except:
                print("no valido.")
            
        print(f" tu edad en 10 años sera {edad_actual + 10}")
                

    
    elif opcion == "3":
        print("saliendo....")
        break


    else:
        print("Opcion no valida, eliga una disponible")