'''Se necesita desarrollar Programa(función)que presupueste cuánto saldrá el alambrado de un
campo. Para ello ingresar las medidas del terrero y el precio del metro de alambre. Crear un
módulo para calcular la cantidad de metros necesarios y calcular el costo del alambrado y
mostrar el costo. '''

from ejercicio10b import presupuesto


largo = int(input("Ingresa la medida del largo del terreno en metros: "))
ancho = int(input("Ingresa la medida del ancho del terreno: "))
metro = int(input("Ingresa el costo del metro de alambre: $"))

presupuesto(largo,ancho,metro)


