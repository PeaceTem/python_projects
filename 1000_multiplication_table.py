#multplication table
from time import sleep
for row in range(1,11):
	for column in range(1,11):
		result = row * column
		print(result,end="  ")
#		sleep(1)
	print("\n")