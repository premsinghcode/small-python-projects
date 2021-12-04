class Animal:
	def __init__(self,name,species):
		self.name = name
		self.species = species
	def __repr__(self):
		return f"{self.name} is {self.species}"

	 	
class dog(Animal):
	def __init__(self,name,species,color):
		self.color = color
		super().__init__(name,species)


b = dog("TIGER","GERMAN SHEPHERD","BROWN")
print(b)

