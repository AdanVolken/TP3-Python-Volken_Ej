def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)

def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]? ")
    if respuesta=="perimetro":
        mostrar_perimetro(la)
    if respuesta=="superficie":
        mostrar_superficie(la)

def validar(dni):
    cantidad=0
    while dni!=0:
        cantidad+=1
        dni//=10
    if cantidad==7 or cantidad==8:
        print("True")
    else:
        print("False")