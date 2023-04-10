'''12- Desarrollar un programa (función) que calcule en interes que nos dará un plazo Fijo para lo
cual se deberá ingresar el Capital, la tasa y la cantidad de días del mismo. Utilizar la Fórmula
de interés simple - (C*R*T)/ 100*UT . Mostrar el interés a percibir.'''

def calculo_interes (cap,tasa,cantidadDias):
    resultado = cap * tasa * cantidadDias / 365
    return resultado

capital = float(input("Ingrese su capital: "))
tasa = float(input("ingrese su tasa de interes: "))
cantidad = float(input("ingrese la cantidad de dias: "))

resultado = calculo_interes(capital, tasa, cantidad)

print("El interes a percibir por el tiempo de: $" ,resultado )