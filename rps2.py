import random
print("Welcome to rock paper scissors game!!!")
move = input("What is your move?")
if move == "rock" or move == "paper" or move == " scissors":
	print("lets see what computer chooses")
else:
	print("pick your choice you asshole!!!!")
r = random.randint(0,2)
if r == 0:
	computer = "rock"
elif r == 1:
	computer = "paper"
elif r == 2:
	computer = "scissors" 
print("computer chose :"  + computer)
if move == computer:
	print("Its a tie")	
elif move == "rock" and computer == "paper":
	print("computer wins ")
elif move == "paper" and computer == "rock":
	print("you win")	
elif move == "paper" and computer == "scissors":
	print("computer wins")		
elif move == "scissors" and computer == "paper":
	print("you win")
elif move == "rock" and computer == "scissors":
	print("you win")	
elif move == "scissors" and computer == "rock":
	print("computer wins")

