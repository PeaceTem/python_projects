# create an account
name = input("What is your name? \n\t")
matric_nos = input("What is your matric number?\n\t")
date_of_birth = input("Your date of birth should be like this: 01012021\nWhen are you born")
username = input("Enter your username:   ")
password = input("Your password should contain a minimum of 6 characters. It should not be the same as neither your username, nor your date of birth, nor your matric nuumber.\nEnter your password:\n\t")
#testing for password validity
while (len(password) < 6 or password == username or password == date_of_birth or password == matric_nos):
	password = input("Your password is invalid, make sure that it satisfies the above specifications.\nEnter your new password:\n\t")
	
	
print("You've succesfully created an account.")




