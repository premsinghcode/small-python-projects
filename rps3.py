import random
a = random.randint(1,10)
guess = None
while(guess!=a):
	guess = input("Guess a number between 1 and 10")
	guess = int(guess)
	if(a>guess):
		print("its too low")
	if(a<guess):
		print("its too high")
	if(a==guess):
		print("you are right")
print(a)		
			



