# convert from base 2 to base10
		
number = input('Enter a number: ')
while not number.isdigit():
	number = input("\nPlease enter a valid number\nEnter your number: ")

base = input("Enter the base number: ")
while not base.isdigit():
	base= input("\nPlease enter a valid number\nEnter your number: ")
total = 0
iterator = 0
number = reversed(number)
for num in number:
	total += int(num) * pow(int(base),iterator)
	iterator += 1
	
print(total)