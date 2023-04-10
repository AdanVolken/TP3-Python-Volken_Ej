'''11- Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios
al principio o al final del string pasado por parámetro.'''

def longitud_ult_palabra (frase):
    
    longPlabra = frase.split()
    return len(longPlabra[-1])

frase = (str(input("Ingrese una frase: ")))

print("Su longitud es: ", longitud_ult_palabra(frase))
