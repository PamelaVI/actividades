"""05-
    Función que reciba como parametros dos números (a y b), y
devuelva una tupla con todos los números primos que se encuentra entre
a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100"""

#numeros primos son divisibles por 1 y por si mismo

#Numeros Primos

#rango de 0 a 100

def numero_primo(a=0, b=100):
	x=1
	while x<=b:
		contador =1
		a=0
		while contador <=x:
			if x % contador ==0:
				a=a+1
			contador =contador +1
		if a ==2:
			print(x)
		x= x+1
		
print(numero_primo())


