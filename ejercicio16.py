
'''
Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera
letra de cada palabra a mayúscula y las demás letras a minúscula, dejando
inalterados los demás caracteres. Precondición: el separador de palabras es el
espacio: " ". Agregar doctests con suficientes casos de prueba para validar que la
función retorna el valor esperado ante distintos argumentos.
'''

def titulo(frase):
    frase = frase.split(" ")
    for i in range(len(frase)):
        frase[i] = frase[i].capitalize()
    return " ".join(frase)


print (titulo("Probando la primera frase para ver si funciona"))
print (titulo("Probando la sefunda frase para ver si funciona!!!!!"))
print (titulo("Por lo que veo esta funcionando perfecto"))
print (titulo("Grupo: Ferronato y Volken tienen 10"))