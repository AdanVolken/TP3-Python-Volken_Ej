a=0
b=0
c=0
def numeros (num1, num2, num3):
	a = int(input("Ingrese nota: "))
	b = int(input("Ingrese nota: "))
	c = int(input("Ingrese nota: "))
	resultado= (a+b+c)/3
	return resultado
total=numeros(a,b,c)
print(total)