"""6-
    Crear una función que reciba una lista de números y elimine
    los valores que se encuentran duplicados de la lista.
    Retornar la lista, y una tupla con los valores que han sido
    eliminados.
"""
#creo un funcion que los elimine a los duplicados
def remove_repetidos(mylista):
	norepetidos=[]
	for n in mylista:
		if n not in norepetidos:
			norepetidos.append(n)
		else:
			mylista.remove(n)
	norepetidos=tuple(norepetidos)
	return norepetidos

#imprimo mi primer lista
mylista=[2,3,5,7,9,10,26,5,7,9,0,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,2,3,4,5]
#remuevo los numeros repetidos y creo otra lista
resultado=remove_repetidos(mylista)
print()
print()
print()
print(resultado)
print(mylista)



