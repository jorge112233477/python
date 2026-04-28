def prueba(num1 , num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")


    for arg in args:
        print(f"arg es igual a {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        

    

lista_args = [5,11,4,45,425,634]
dic_kwargs = {"x" : 3, "y" : 4, "z" : 5}


prueba(5,11,*lista_args, **dic_kwargs)