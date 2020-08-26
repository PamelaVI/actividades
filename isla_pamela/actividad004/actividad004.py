"""Un programa que permita escribir varios modelos de cartas/notas
y que después pueda seleccionar un modelo de nota, y que me generé
varias notas reemplazando los destinatarios con una lista de nombres
que se le pase y el nombre del remitente indicado.
    
    Ej:
    ----
        Estimado (nombre):
            Le damos la bienvenida al servicio.

        Con afecto,
            (nombre_remitente)
    ----

    Pasandole lista destinatarios: Juan, Sandra y Jorge.
        Y remitente Axel.

    ----
        Estimado Juan:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----
        Estimado Sandra:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel
    ----

        Estimado Jorge:
            Le damos la bienvenida al servicio.

        Con afecto,
            Axel """

print("*******************************************************************")
print("**************Bienvenido al servicio de notas rapidas**************".upper())
print("*******************************************************************")            
print()
print("Que desea realizar?")
print("En la pantalla podra observar los modelos disponibles ")
nota1=("El modelo de nota disponible es:\nEstimado destinatario\nLe damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto remitente".center(50))
print()
carta1=("El modelo de carta disponible es:\nEstimado destinatario\nEl motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34\nAqui  pactaremos su financiacion\nSin otro en particular me despido atentamente esperando su respuesta\nremitente".center(50))
print()
TuEstilo1=("El modelo de TuEstilo ,esta diseñado para que usted la cree:\nEstimado destinatario\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\nremitente".center(50))
print(nota1)
print()
print(carta1)
print()
print(TuEstilo1)
remitente=[]
destinatario=[]
nombre= None
while nombre !=1:
    nombre=input("Ingresa el Apellido y Nombre del Remitente: ")
    if nombre == "":
        remitente.append(nombre)
        print(remitente)
    else:
        print("Sigamos...")
        break
        for i in range(len(remitente)):
                print(remitente)

        
ingresar= None
while ingresar !="fin":
    ingresar=input("Ingresa el Apellido y Nombre del destinatario: ")
    if ingresar == "fin":
        break
    else:
        if ingresar ==" ":
            destinatario.append(ingresar)
            print(destinatario)
            break
            for i in range (len(destinatario)):
                print(destinatario)

print()
print()            
print("1-Nota 2- Carta 3-Tu Estilo")


opcion=None

while opcion !=None:
    nota=("Estimado{} \n:Le damos la bienvenida al servicio de atencion al cliente\nEl motivo de mi nota es recordarle el vencimiento de su cuenta\nCon afecto.{}".format(destinatario,remitente).center(50))
    carta=("Estimado{} \n:El motivo de mi carta es solicitar que se acerque a las oficinas cito en calle 20 entre 23 y 34 para pactar financiacion\nSin otro en particular me despido attentamente esperando su respuesta.{}".format(destinatario,remitente).center(50))
    TuEstilo=("Estimado{}:\nEl motivo.................................................\n....................................\n....................................\n....................................\nSin otro en particular me despido atentamente esperando su respuesta\n{}".format(destinatario,remitente).center(50))
    opcion=input("Ingrese el tipo de tramite que desea realizar:")
    if opcion ==1:
        for i in range (destinatario):
            for ingresar in destinatario:
                "{}".format(ingresar)
                print (nota)
    if opcion==2:
        for i in range (destinatario):
            for ingresar in destinatario:
                "{}".format(ingresar)
                print(carta)
    if opcion ==3:
        for i in range (destinatario):
            for ingresar in destinatario:
                "{}".format(ingresar)
                print(ingresar)
   


"""
respuesta = None
while respuesta != 0:
    print(
    1Submenu
    0Salir
    )
    respuesta = int(input("Respuesta: "))
    if respuesta == 0:
        print("Saliendo...")
        break
    elif respuesta == 1:
        respuesta2 = None
        while respuesta2 != 0:
            print(   
                1) Sub
                0) Salir
                )
            respuesta2 = int(input("Respuesta: "))
            if respuesta2 == 0:
                print("Volviendo...")
                break
            elif respuesta2 == 1:
                print("Opción Sub")
            else:
                print("Opción no válida, otra vez")
    else:
        print("Opción no válida, jeje, again")
"""