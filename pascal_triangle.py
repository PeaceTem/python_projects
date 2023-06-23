# pascal's triangle
# factorial function
def fac(n):
	if n == 0:
		return 1
	elif n > 0:
		return n * fac(n - 1)
	else:
		print("An error occurred")
# permutation function
def perm(m,n):
	return fac(m)//fac(m - n)
# combination function
def comb(m,n):
	return perm(m,n)//fac(n)	

length_of_triangle = int(input("Enter the length of the triangle:  "))

for number in range(0, length_of_triangle + 1):
	for count in range(0, number + 1):
		level = comb(number, count)
		if count == number:
			print(level)
		else:
			print(level, end=" ")
	