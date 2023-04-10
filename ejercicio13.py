'''13- Realizar un programa usando funciones que permita administrar carpetas y archivos. De
acuerdo a la función seleccionada llamar a la función correspondiente.
'''
'''with open('ejercicio 13.txt', 'w') as p:   #Esto se usa para crear una carpeta
    p.write("Hola Mundo?") '''

def carpeta_existe(f):
    import os
    os.path.exists(f)
    return f
    
f=input("Ingrese nombre de la carpeta para ver si existe: ")
carpeta_existe(f)
#print(carpeta_existe(f))