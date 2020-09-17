import random

palabras=["hormiga","perro","oso","abeja",
"caballo", "gato", "tigre","mano","mono",
"bizcocho", "tomate","agua","mago","amigo",
"miel","piedra","avispa","caballero","tortuga" ,"tortilla"]

#pantalla de bienvenida
print("*****************************")
print("***   JUEGO DEL AHORCADO  ***")
print("*****************************")
print()
print()
nombre=input("¿Como te llamas?: ")#pregunto el nombre
print("Hola, "+nombre)#saludo segun el nombre 
print("")#imprime un espacio

print("**** 1-Jugar **** ")#presentacion de las opciones 
print("**** 0- Salir ****")
print()
#introduccion, pregunto si quiere jugar o no
opcion=None
while opcion !=0:
	opcion=int(input("Ingrese una opcion: "))
	if opcion == 0:
		print ("Gracias, nos vemos.Saliendo....")
		break 
	else:
		if opcion==1:
			print("Juguemos...") 
			
	palabra= random.choice(palabras)
	horca=["""
	============
	+------+
	|      |
	|      |
	|
	|
	|
	|
	|
	|
	| 
	|
	==============
	"""]
			
	ahorcado=["""
	==============
	+------+
	|      |
	|      O 
	|     /|\
	|    / | \
	|      |
	|     / \
	|    /   \
	|
	==============
	"""]
	print()
	fallos=0
	resultado=[]
	intentos=5
	jugar = True
	for i in range(fallos):
		fallos.append(horca)
		print(ahorcado[1])
	for i in range(len(horca)-fallos):
		print(horca[i+fallos])
	print("")
	
	print("     ",end="")
	for i in resultado:
		print(i,end="")
	print("")
	
	if resultado==palabra:
		print("HAS GANADO. :-) :-)")
	
	if fallos==6:
		print("La palabra era:{}".format(palabra))
		print("*****HAS PERDIDO***** ")
	
	tupalabra=" "
	intentos=5
	resultado=[]
	for i in range(len(palabra)):
		resultado.append("-")
		while intentos >0:
			fallos=0
			for letra in palabra:
				if letra in tupalabra:
					print(letra, end="")
			for letra in enumerate(palabra):
				if letra==palabra:
					resultado=palabra
				else:
				    print("-",end= "")
				    fallos +=1
			
			if fallos==0:
				print("")
				print("FELICIDADES, GANASTE")
				print("")
			
			tuletra=str(input("Introduce una letra: "))
			tupalabra +=tuletra
			
			if tuletra not in palabra:
				intentos -=1
				print("Te equivocaste")
				print("Te quedan {}intentos".format(intentos))
			
			if fallos==0:
				print("")
				print("Felicidades")
				print("")
			
			if intentos==0:
				print(ahorcado[intentos])
		else:
			print("Gracias por participar")
			break
		
		