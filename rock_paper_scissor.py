#This us a rock paper scissor game
import random
while True:
	type = ["rock","paper","scissor"]
	print("1 - rock \n2 - paper \n3 - scissor")
	trial = 3
	while trial > 0:
		guess = int(input("Enter a choice: "))
		while guess not in range(1,4):
			guess = int(input("Enter a choice: "))
		pos = random.randint(0,len(type) - 1)
		print("Computer:\n",type[pos],"\nYou:\n",type[guess - 1])
		if type[guess - 1] == type[pos] :	
			print("You won!")
			trial = 3
		else:
			print("You lose!")
			trial -= 1
	