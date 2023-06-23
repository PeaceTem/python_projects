# convert from base 10 to any base
while 1:
	number = input('Enter a number: ')
	while not number.isdigit():
		number = input("\nPlease enter a valid number\nEnter your number: ")

	base = int(input("Enter the base: "))
	total = ""
	print(number)
	number = int(number)
	while number >= 1:
		total += str(number % base)
		number = number // base

	print(total[::-1])


