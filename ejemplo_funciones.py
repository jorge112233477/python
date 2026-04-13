lista_cafe = [("cafe1", 3.4) , ("cafe2" ,  3) , ("cafe3" , 2.4)]



def encontrar_cafe_mas_caro(lista):
    precio_mayor = 0
    cafe_mas_caro = ""


    for c,p in lista:
        if p > precio_mayor:
            precio_mayor = p
            cafe_mas_caro = c



    return cafe_mas_caro, precio_mayor

cafe, precio = (encontrar_cafe_mas_caro(lista_cafe))
print(cafe, precio)

print(f"el cafe mas caro es {cafe} y su precio es {precio}")