def repetido(*arg):

    for i in range(len(arg) - 1):
        if arg[i] == 0 and arg[i+1] == 0:
            return True
        

        else:
            return False
        


resultado = repetido(0,0,64,7,0,0, 42,56,53)
print(resultado)
