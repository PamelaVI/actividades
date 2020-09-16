#actividad4
lista_destinatario0["axel","alan","sandra"]
remitente="pedro"

modelo_elegido="hola(destintario)soy (remitente),chau(destinatario),firma:(remitente)"


	def renderizar_cartas(lista_destinatario,mensaje):
		for destinatario in lista_destinatario:
			carta_imprimir=modelo_elegido.replace("(destinatario)",destinatario)
			carta_imprimir=carta_imprimir.replace("(remitente)",remitente)
			print(carta_imprimir)

renderizar_cartas(modelo_elegido,lista_destintario,remitente)

#si tenemos lista vacia 
def renderizar_cartas(lista_destinatario,mensaje)
for deetinatario in lista_destinatario:
carta_imprimir=modelo_elegido.replace("(destinatario)",destinatario)
carta_imprimir=carta_imprimir.replace("(remitente)",remitente)
print(carta_imprimir
sigue_carga=True 
while sigue_carga:
persona=input("ingrese nombre destintario(deje vacio para cortar la carga)")
if persona=""
sigue_carga=false
else:
lista_destinatario.append(persona)

remitente=input("Ingrese:")
renderizar_cartas(modelo_elegido,lista_destintario,remitente)

while sigue_carga:
modelo_ingresar=input("ingrese nombre destintario(deje vacio para cortar la carga)")
if pmodelo_ingresar=""
sigue_carga=false
else:
lista_modelo.append(modelo_ingresar)

#para elegir los modelos
modelo1=["ol"]
modelo2=["hola"]
modelo3=[""]
lista_modelos=[modelo1,modelo2,modelo3]



sigue_carga=True
while sigue_carga:
persona=input("ingrese nombre destintario(deje vacio para cortar la carga)")
if persona=""
sigue_carga=false
else:
lista_destinatario.append(persona)

remitente=input("Ingrese:")


for modelo in enumerate(lista_modelos):
print(indice,end"-")
print(modelo)

opcion=int(input("seleccione: "))
modelo_elegido=lista_modelo(opcion)

renderizar_cartas(modelo_elegido,lista_destintario,remitente)



opcion=("Ingrese el tipo de modelo a usar:")


while opcion !=0:
    nota=("Estimado{} \n:Le damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto.{}".format(destinatario,remitente).center(50))
    carta=("Estimado{} \n:El motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34 para pactar financiacion\nSin otro en particular me despido attentamente esperando su respuesta.{}".format(destinatario,remitente).center(50))
    TuEstilo=("Estimado{}:\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\n{}".format(destinatario,remitente).center(50))
    if 1==nota:
        for i in destinatario:
            for ingresar in destinatario:
                "{}".format(ingresar)
                print (nota*len(destinatario[ingresar]))
                print("usted eligio nota")
    if 2==carta:
        for i in destinatario:
            for ingresar in destinatario:
                "{}".format(ingresar)
                print (carta*len(destinatario[ingresar]))
                print("usted eligio cata")
    if 3 ==TuEstilo:
        for i in destinatario:
            for ingresar in destinatario:
                "{}".format(ingresar)
                estilo=int(input("Escriba su nota:"))
                print("estilo".join(TuEstilo))
                print(TuEstilo*len(destinatario[ingresar]))
                print("usted eligio su estilo")
            for ingresar in destinatario:
            	carta_imprimir=modelo_elegido.replace("(destinatario)",destinatario)
            	carta_imprimir=carta_imprimir.replace("(remitente)",remitente)
            	print(carta_imprimir)
          
            for modelo in enumerate(lista_modelos):
            	print(indice,end="-")
            	print(modelo)

            	"""