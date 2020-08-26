import actividad002 

print("*****Bienvenidos*****")
tiempo=int(input("Ingrese  los segundos: "))
print("")
print(actividad002.reloj(tiempo))
print("")
print("La cantidad de segundos son,horas{},minutos{},segundos{}".format(horas,minutos,segundos))

minutiño=int(input("Cuantos minutos:"))
segund=relojero(minutos=minutiños)
print(actividad002.reloj(segund))
print("")

tiempito=input("Horas :minutos   : segundos :")
h,m,s=tiempito.split(":")
h=int(h)
m=int(m)
s=int(s)
print("Horas",h)
print("Minutos",m)
print("Segundos",s)
print(actividad002.relojero(h,m,s))
