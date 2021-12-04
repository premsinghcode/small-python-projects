import random
a = 0
b = 0
computer = ""
while a <2 and b <2:
	r = random.randint(0,2)
	if r == 0:
		computer = "rock"
	elif r == 1:
		computer = "paper"
	elif r == 2:
		computer = "scissors"
	choice = input("what do you choose")
	
	if a == "rock" and b == "scissors":
		print("player  wins!!!!!!")
		a +=1
	elif a == "scissors" and b == "rock":
		print("computer wins!!!!!!")
		b+=1
	elif a == "paper" and b == "rock":
		print("player  wins!!!!!!")
		a+=1
	elif a == "rock" and b == "paper":
		print("computer  wins!!!!!!")	
		b+=1	
	elif a == "scissors" and b == "paper":
		print("player  wins!!!!!!")
		a+=1
	elif a == "paper" and b == "scissors":
		print("computer wins ")
		b+=1
	if(a>b):
		print("You win")
	else:			
		print("computer wins")