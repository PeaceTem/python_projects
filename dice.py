# this is a dice rolling game
# Thank you CSC guys for your support

import random
while True:
	answer = input("Press 1 for 'yes' or any character for no: ")

	if answer == "1":
		print("%s"%random.randint(1,6))
	else:
		quit()