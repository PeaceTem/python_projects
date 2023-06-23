#A program to check eligible voters
age_voter = int(input("Enter the age of the voter: "))
if age_voter >= 18:
	print("The voter is eligible to vote.")
else:
	print("The voter is not eligible to vote.")