	
print("*******************************************************************")
print("**************Bienvenido al servicio de notas rapidas**************".upper())
print("*******************************************************************")            
print()
def renderizar_cartas(lista_destinatario,mensaje):
	for destinatario in lista_destinatario:
		carta_imprimir=modelo_elegido.replace("(destinatario)",destinatario)
		carta_imprimir=carta_imprimir.replace("(remitente)",remitente)
		print(carta_imprimir)
modelo1="Estimado(destinatario)\n:Le damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto (remitente)"
modelo2="Estimado(destinatario)\n:El motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34 para pactar financiacion\nSin otro en particular me despido attentamente esperando su respuesta.(remitente)"
modelo3="Estimado(destinatario):\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\n(remitente)"
print()
lista_modelos=[modelo1,modelo2,modelo3]
print()
sigue_carga=True 
while sigue_carga:
	modelo_ingresar=input("Ingrese modelo : (destinatario) para destinatario(remitente) para remitente  (vacio para cortar)")
	if modelo_ingresar ==" ":
		sigue_carga=False
	else:
		lista_modelos.append(modelo_ingresar)

print()
lista_destinatario=[]
print()
sigue_carga=True
while sigue_carga:
	persona=input("ingrese nombre destintario(deje vacio para cortar la carga)")
	if persona ==" ":
		sigue_carga=False
	else:
		lista_destinatario.append(modelo_ingresar)
print()
print()
remitente=input("Ingrese nombre del remitente:")
print()
for indice,modelo in enumerate(lista_modelos):
	print(indice,end="-")
	print(modelo)
print()
print()
opcion=int(input("seleccione un tipo de modelo: "))
modelo_elegido=lista_modelo[opcion]




renderizar_cartas(modelo_elegido,lista_destintario,remitente)



























































opcion=("Ingrese el tipo de modelo a usar:")
while opcion !=0:
    nota=("Estimado{} \n:Le damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto.{}".format(persona,nombre).center(50))
    carta=("Estimado{} \n:El motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34 para pactar financiacion\nSin otro en particular me despido attentamente esperando su respuesta.{}".format(persona,nombre).center(50))
    TuEstilo=("Estimado{}:\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\n{}".format(persona,nombre).center(50))
    if 1==nota:
        for persona in lista_destinatario:
            for persona in lista_destinatario:
                "{}".format(persona)
                print (nota*len(lista_destinatario[persona]))
                print("usted eligio nota")
    if 2==carta:
        for persona in lista_destinatario:
            for persona in lista_destinatario:
                "{}".format(persona)
                print (carta*len(lista_destinatario[persona]))
                print("usted eligio cata")
    if 3 ==TuEstilo:
        for persona in lista_destinatario:
            for persona in lista_destinatario:
                "{}".format(persona)
                estilo=int(input("Escriba su nota:"))
                print("estilo".join(TuEstilo))
                print(TuEstilo*len(lista_destinatario[persona]))
                print("usted eligio su estilo")


lista_modelos=[nota,carta,TuEstilo]

nombre= None
while nombre !=1:
    remitente=[]
    nombre=input("Ingresa el Apellido y Nombre del Remitente: ")
    if nombre == "":
        remitente.append(nombre)
        print(remitente)
    else:
        print("Sigamos...")
        break
cargar=True
while cargar:
    lista_destinatario=[]
    persona=input("Ingresa el Apellido y Nombre del destinatario: ")
    print(" Al ingresar fin el sistema dejara de almacenar los nombres de los destinatarios ")
    if persona == "":
    	cargar== False
    	break
    else:
    	lista_modelos.append(opcion)

            
for ingresar in destinatario:
            	carta_imprimir=modelo_elegido.replace("(destinatario)",destinatario)
            	carta_imprimir=carta_imprimir.replace("(remitente)",remitente)
            	print(carta_imprimir)