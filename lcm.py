# This is used to find lcm of many numbers
while 2:
	numbers = []
	number = 1
	while number != '0':
		number = input("Enter a number, or press '0' to end input: ")
		numbers.append(int(number))
	#removing 0 from the list
	numbers.remove(0)
	highest_num =max(numbers)
	result = False
	while result == False:
		result = True
		for elem in numbers:
			if highest_num % elem != 0:
				result = False
		if result == True:
			break
		highest_num += 1
	print("The LCM is",highest_num)