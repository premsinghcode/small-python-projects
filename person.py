class Person:
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age
	def greeting(self):
		return f"Hello {self.first} {self.last}. I guess you age is {self.age}"
a = Person("PREM","SINGH",17)	
print(a.greeting())	
		
		
