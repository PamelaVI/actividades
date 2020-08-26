"""05-
    Función que reciba como parametros dos números (a y b), y
devuelva una tupla con todos los números primos que se encuentra entre
a y b (incluyendo a y b si son primos).
    Por defecto a=0, y b=100"""

#numeros primos son divisibles por 1 y por si mismo

def generar_primos(a=0,b=100):
	nupri=2
	for num in range(2,b+1):
		for nupri in nupri:
			if num %i==0:
				break
		else:
			nupri.append(num)




"""


	while True:
		verifico=b+1

		contador+1

		divisores=0

		while contador <= verifico:
			if verifico%divisores ==0:
				divisores+=1
			if divisores>2:
				break

			contador +=1
		if divisores ==2:
			return verifico
			numero=verifico

generador=generar_primos()
primos=(next.generador()for a in and range )



def primo(a=0,b=100):
	numeros=[2,3,5,7]
	for x in range (a,b):

	if num<1:
		return False
	elif num==2:
		return True
	else:
		for i  in range(2,num):
			if num %i==0:
				return False
		return True
		resultado=primo(num)
			return primo


datos= 23,45
print(primo(datos))

"""