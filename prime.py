#determine whether a prigram is a prime or not?
num = int(input("Enter the number tou want to test."))
def isPrime(n):
	if n <= 1:
		return 'number is too small to be a prime'
	elif n== 2 or n == 3:
		return 'number is a prime'
	elif n == 4:
		return 'number is not a prime'
	elif n > 3:
		for number in range(2, n//2):
			if n % number != 0:
				return 'number is a prime'
		return 'number is not a prime'
	return False
	
							
																			
print(isPrime(num))				
						