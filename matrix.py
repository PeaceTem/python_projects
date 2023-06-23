#matrix
print("a  b  c\ne  f  g\nh  i  k")
a = int(input("Enter a:  "))
b = int(input("Enter b:  "))
c = int(input("Enter c:  "))
first_row =[a,b,c]
e = int(input("Enter e:  "))
f = int(input("Enter f:  "))
g = int(input("Enter g:  "))
second_row = [e,f,g]
h = int(input("Enter h:  "))
i = int(input("Enter i:  "))
k = int(input("Enter k:  "))
third_row = [h,i,k]
matrix = [first_row, second_row, third_row]
#printing out the matrix.
for row in matrix:
	for element in row:
		print(element, end=("  "))
	print("\n")
#printing all the elements in the first row
print("The elements in the first row are: \n")
for element in first_row:
	print(element, end=("  "))
print("\n")
#printing the minimum value of the second row
print("The minimum value of the second row is: ",min(second_row))
#printing the maximum value of the left diagonal
print("The maximum value of the left diagonal is: ",max(a, f, k))
# the transpose block
print("The transpose of the matrix is:\n")
transpose = []
position = 0

while position < 3:
	row = []
	for element in matrix:
		row.append(element[position])
	transpose.append(row)
	position += 1
	
for row in transpose:
	for element in row:
		print(element, end=("  "))
	print("\n")
#the maximum value of the matrix

maximum = 0
for row in matrix:
	for element in row:
		if maximum < element:
			maximum = element

print("The maximum element in the matrix is: ",maximum)
#the minimum value of the matrix
minimum = maximum
for row in matrix:
	for element in row:
		if minimum > element:
			minimum = element
			
print("The minimum element in the matrix is: ",minimum)