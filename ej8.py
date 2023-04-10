def maximo(a,b):
    if a>b:
        return a
    else:
        return b

def minimo(a,b):
    if a<b:
        return a
    else:
        return b


#programa principal
x=int(input("Un número: "))
y=int(input("Otro número: "))
print(maximo(x-3, minimo(x+2, y-5)))

# La solucion a este ejercicio es que las funciones tenian los parametros a y b, y dentro de ella usaban x e y
# por ende no iba a funcionar jamas, porque no estaba correcta la sintaxis.