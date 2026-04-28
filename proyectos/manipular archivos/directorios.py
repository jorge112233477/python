from pathlib import Path

carpeta = Path("C:/Users/Neo-PC/Desktop/python/proyectos/manipular archivos/prueba.txt")



print(carpeta.read_text()) # this line print in console every contend 

print(carpeta.suffix) # extract the extension 

print(carpeta.stem) # extract the file without extension


print(carpeta.exists()) # check the file if exists or not


if not carpeta.exists():
    print("not exists")

else:
    print("if exits")