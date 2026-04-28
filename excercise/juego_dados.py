import random

def lanzar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    return dado1, dado2
    

d1, d2 = lanzar_dados()
    
    

def evaluar_jugada(d1,d2):
    
    suma_dados = d1 + d2
    
    if suma_dados  <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
        
    
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
        
        
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"
    

