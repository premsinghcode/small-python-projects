class Card:
	def __init__(self,value,suit):
		self.value = value
		self.suit = suit
	def __repr__(self):
		a = f"{self.value} of {self.suit}"
		return a	