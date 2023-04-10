def DNIvalido(dni):
    cantidad=0
    while dni!=0:
        cantidad+=1
        dni//=10
    return cantidad==7 or cantidad==8

def lenUltimaPalabra(cadena):
    longitud=len(cadena)
    if longitud==0:
        return 0
    cantidad=0
    for i in range(longitud):
        if cadena[i]!=' ':
            cantidad+=1
        else:
            if cadena[i]==' ' and i<(longitud-1) and cadena[i+1]!=' ':
                cantidad=0
    return cantidad

def primerosTres(numero):
    while numero >= 1000:
        numero = numero // 10  # el operador // divide y da resultado entero, es por eso que no hay que pasar a int(numero) al retornarla
    return numero

def obtenerIdentificador(nombre, dni):
    nombre= nombre.strip()  # esta funcion elimina los espacios en blanco que puede apretar el usuario al ingresar
    id=nombre[0:nombre.find(" ")]  #
    id= id+str(lenUltimaPalabra(nombre))  # utilizo la funcion con len y le paso el nombre como parametro
    id= id+str(primerosTres(dni))   # los convertimos a str pq no podemos concatenar un string con un numero
    return id 


nombre=input("Ingrese el nombre del socio: ")
while nombre!="":
    dni= int(input("Ingrese el DNI: "))
    while not (DNIvalido(dni)):   # Mientras no sea valido el dni que entre en el bucle, el not invierte un valor boleeano. Tmb podriamos poner (validar(dni))==False
        print("DNI invalido")
        dni= int(input("Ingrese el DNI: "))
    identificador =obtenerIdentificador(nombre, dni)    # la funcion obtenerIdentificador la ponemos dentro de una variable, y usa como parametro para ejecutarse (nombre, dni)
    print("El identificador del socio es: ", identificador)
    nombre=input("Ingrese el nombre del socio: ")

