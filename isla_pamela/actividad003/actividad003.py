# Crear una clase Persona, que tenga atributo nombre y apellido, y los metodos get y set para cada atributo.

class Persona():
	def __init__(self,nombre,apellido):
		self.nombre=nombre
		self.apellido=apellido


	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def setNombre(self,n_nombre):
		self.nombre=n_nombre

	def setApellido(self,n_apellido):
		self.apellido=n_apellido

	def toString(self):
		return "nombre: "+self.nombre + "apellido: "+self.apellido




