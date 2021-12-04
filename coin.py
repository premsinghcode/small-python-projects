import random
def coin_flip():
	coin = random.randint(0,1)
	return coin

coin = coin_flip()	
if coin == 0:
	print("head")
else:
	print("tail") 	

