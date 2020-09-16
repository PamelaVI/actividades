#Un programa que permita escribir varios modelos de cartas/notas
#y que después pueda seleccionar un modelo de nota, y que me generé
#varias notas reemplazando los destinatarios con una lista de nombres
#que se le pase y el nombre del remitente indicado.
    
 #   Ej:
  #  ----
   #     Estimado (nombre):
    ##   Con afecto,
      #      (nombre_remitente)
    #----

    #Pasandole lista destinatarios: Juan, Sandra y Jorge.
     #   Y remitente Axel.

    #----
     #   Estimado Juan:
      #      Le damos la bienvenida al servicio.
# Con afecto,
 #           Axel
  #  ----
   #     Estimado Sandra:
    #        Le damos la bienvenida al servicio.
#   Con afecto,
 #           Axel
  #  ----

   #     Estimado Jorge:
#            Le damos la bienvenida al servicio.
#       Con afecto,
 #           Axel 

print("*******************************************************************")
print("**************Bienvenido al servicio de notas rapidas**************".upper())
print("*******************************************************************")            
print()
print("**En la pantalla podra observar los modelos disponibles de notas rapidas**")
nota1=("El modelo de nota disponible es \nEstimado destinatario\nLe damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto remitente".center(50))
print()
carta1=("El modelo de carta disponible es\nEstimado destinatario\nEl motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34\nAqui  pactaremos su financiacion\nSin otro en particular me despido atentamente esperando su respuesta\nremitente".center(50))
print()
TuEstilo1=("El modelo de TuEstilo ,esta diseñado para que usted la cree\nEstimado destinatario\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\nremitente".center(50))
print(nota1)
print()
print(carta1)
print()
print(TuEstilo1)
print()
print()
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
       
ingresar= None
while ingresar !="fin":
    destinatario=[]
    ingresar=input("Ingresa el Apellido y Nombre del destinatario: ")
    print(" Al ingresar fin el sistema dejara de almacenar los nombres de los destinatarios ")
    if ingresar == "fin":
        break
    else:
        if ingresar ==" ":
            destinatario.append(ingresar)
            print(destinatario)
        for i in range(len(destinatario)):
            print(destinatario)
            break

print(remitente)
print()
print(destinatario)

print()
print()
print("1-Nota 2- Carta 3-Tu Estilo")
print()
print()
print("Que desea realizar?")
print()
print()
opcion=input("Ingrese el tipo de tramite que desea realizar:")



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


   




print()
print()            

