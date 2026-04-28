def reducir_lista(lista):
    lista = list(set(lista))
    lista.remove(max(lista))
    return lista
    
    
   
    
    
    
    
def promedio(lista):
    return sum(lista) / len(lista)
    
    

lista_numeros = [1,2,3,4,5,6,7]


lista_reducida = reducir_lista(lista_numeros)
resultado = promedio(lista_reducida)

print(lista_reducida)
print(resultado)