def descuento (importe):
    if importe >= 15000 and importe < 30000:
        print("Se le realiza un descuento del 8%")
        return importe * 0.08
    elif importe >= 30000 :
        print("Se le realiza un descuento del 15%")
        return importe * 0.15
    else:
        print("No hay decuentos")
        return 0


cant=int(input("Ingrese la cantidad de articulos que comprara: "))
importeTotal = 0

for i in range (cant):
    articulo= input("Ingrese el nombre del articulo: ")
    cantidad= int(input("Ingresa la cantidad que va a comprar: "))
    precio= int(input("Ingrese el precio del producto: "))
    total = cantidad*precio

    importeTotal = total + importeTotal

    print("El importe a pagar de este articulo es de: ", total)

# importe = importeTotal (total)
print("Factura: ", importeTotal)
descuento= descuento(importeTotal)
print("El descuento en este caso es de $: ", descuento)