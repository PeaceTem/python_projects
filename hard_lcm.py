
def prime(n):
		if n == 4:
			return False
		for num in range(2,n//2):
			if n % num == 0:
				return False
		return True					

					
numbers = []
number = 1
while number != '0':
	number = input("Enter a number, or press '0' to end input: ")
	numbers.append(int(number))
#removing 0 from the list
numbers.remove(0)
highest_num =max(numbers)			
print(numbers, highest_num)		
primes = []
def usePrime(num):
	for element in range(2, num + 1):
		if prime(element):
			primes.append(element)
	
	
usePrime(highest_num)
print(primes)

while True:
	for i in numbers:
		for j in primes:
			if i % j == 0:
				