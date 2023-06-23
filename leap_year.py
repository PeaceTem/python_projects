#This is a program to check if a year is a leap year
#the first leap year was 1752
#a leapbyear is divisible by 4
#a century year is a leap year when it is divisible by 400
year = int(input("Enter the year: "))
output_year = year

if year in range(1752,):
	if year % 100== 0:
		year /= 100
	
	if year % 4 == 0:
		print(output_year, "is a leap year.")
else:
	print(output_year, "is not a leap year.")