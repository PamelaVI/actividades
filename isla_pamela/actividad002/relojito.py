from actividad002 import reloj 
from actividad002 import relojero 
print("*****Bienvenidos*****")
tiempo=int(input("Ingrese  los segundos: "))
print("")
print(reloj(tiempo))
print("")

minutito=int(input("Cuantos minutos:"))
segs=relojero(minutos=minutito)
print(reloj(segs))
print("")

tiempito=input("Horas :minutos   : segundos :")
h,m,s=tiempito.split(":")
h=int(h)
m=int(m)
s=int(s)
print("Horas",h)
print("Minutos",m)
print("Segundos",s)
print(relojero(h,m,s))
