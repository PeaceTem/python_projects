# This section of the code contains all the functions needed
#name  : Akande Olumide
#total time spent: roughly 4 hours

#time spent for withdrawal menu: roughly 1 hour
def withdrawal_menu():
	print("\nWithdrawal menu\n\t1 - N1000\t2 - N2000\n\t3 - N5000\t4 - N10000\n\t5 - N20000\t6 - Cancel transaction\n*****★************★**********★**********★\n")
	
	while True:
		choice2 = input("\nEnter your choice: ")
		#checking if the input is not an integer
		while not choice2.isdigit():
			choice2 = input("\nPlease enter a valid number.\n\nEnter your choice: ")
		#checking if the input is within 1 to 6
		choice2 = int(choice2)
		while choice2 not in range(1,7):
			choice2 = int(input("\nPlease try to input a number in range of 1 - 6;\n\nEnter your choice: "))
			
		#the main withdrawal process
		global customer_balance
		if choice2 == 1:
			if customer_balance < 1000:
				print("\nYour account balance is lower than 1000\n\nTry to deposit money to your account")
			else:
				customer_balance = customer_balance - 1000
				print("\nYou've just withdrew 1000 naira from your account\n\nYour account balance is ",customer_balance)
				
		elif choice2 == 2:
			if customer_balance < 2000:
				print("\nYour account balance is lower than 2000\n\nPlease try to enter a choice that is less than 2000")
			else:
				customer_balance = customer_balance - 2000
				print("\nYou've just withdrew 2000 naira from your account\n\nYour account balance is ",customer_balance)
				
		elif choice2 == 3:
			if customer_balance < 5000:
				print("\nYour account balance is lower than 5000\n\nPlease try to enter a choice that is less than 5000")
			else:
				customer_balance = customer_balance - 5000
				print("\nYou've just withdrew 5000 naira from your account\n\nYour account balance is ",customer_balance)
				
		elif choice2 == 4:
			if customer_balance < 10000:
				print("\nYour account balance is lower than 10000\n\nPlease try enter a choice that is less than 10000")
			else:
				customer_balance = customer_balance - 10000
				print("\nYou've just withdrew 10000 naira from your account\n\nYour account balance is ",customer_balance)
				
		elif choice2 == 5:
			if customer_balance < 20000:
				print("\nYour account balance is lower than 20000\n\nPlease try to enter a choice that is less than 20000")
			else:
				customer_balance = customer_balance - 20000
				print("\nYou've just withdrew 20000 naira from your account\n\nYour account balance is ",customer_balance)	
						
		elif choice2 == 6:	
			print("\nWithdrawal Transaction Cancelled\n\nNo Amount Deducted\nYour balance is ", customer_balance)
			 #returning to the main menu after cancellation
			main_menu()  
			
#time spent for the deposition menu: roughly 30 minutes	
def deposition():
	global customer_balance
	print("\nPlease, enter the amount you want to deposit in naira or enter 0 to terminate transaction\n\n★**********★**********★**********★\n")
	deposit_amount = input("\t")
	#checking if the input is an integer
	while not deposit_amount.isdigit():
		deposit_amount= input("Please enter a valid number. ")
	#the main deposition process
	deposit_amount= int(deposit_amount)
	if deposit_amount == 0:
		#returns to the main menu if the user enter 0
		main_menu() 
	elif deposit_amount != 0:
		customer_balance += deposit_amount
		print("\nYou've deposited, ",deposit_amount," into your account.\n\nYour account balance is now #",customer_balance,"\n\nEnter 0 to go back to the main menu")
		#remains in the deposition menu if the user doesn't input 0'
		deposition() 
		
#time spent for the main menu: roughly 1 hour
def main_menu():
	print("Main Menu:\n\t1. View my Account balance\n\t2. Withdraw cash\n\t3. Deposit  funds\n\t4. Exit\n★********★*******★**********★**********★\n")
	choice1 = input("\nEnter your choice: ")
	#testing the input robustly
	while not choice1.isdigit():
		choice1 = input("\nPlease enter a valid number.\nEnter your choice: ")
	choice1 = int(choice1)
	while choice1 not in range(1,5):
		choice1 = int(input("\nPlease try to input a number in range of 1 - 4;\n\nEnter your choice: "))
		
	global customer_balance
	if choice1 == 1:
		print("\nYour account balance is #",customer_balance,"\n\nEnter 4 to finish all your transactions.\n")
		#this is a self-invoking function, it returns to the main menu screen
		main_menu()    
	elif choice1 == 2:
		withdrawal_menu() #withdrawal function
	elif choice1 == 3:
		deposition()  #deposition function
	elif choice1 == 4:
		global customer_no
		#storing the customer's name'
		customers[customer_no]["customer_balance"] = customer_balance
		for elem in customers:	
			print(elem)
		customer_no += 1
		print("\nThanks, but you can come back anytime soon\n\n★**********★**********★**********★*********★\n") 
		login()
		
#time spent for the login section: roughly 1.5 hours		
def login():
	global customer_no
	print("You are welcome to ABC Bank.\n\nPlease kindly follow the necessary procedure\n\n★**********★**********★**********★**********★")
	customers.append({})
	name = input("\nWhat is your name: ")
	customers[customer_no]["name"] = name
	login_attempt = 3
	#testing for valid account number
	while login_attempt > 0:
		customer_acct_no = input("\nYour account number must be 10 digits long.\n\nEnter your account number: ")
		while not customer_acct_no.isdigit():
			customer_acct_no = input("\nPlease enter a 10 digits number\nEnter your account number: ")
		if len(customer_acct_no) == 10:
			customers[customer_no]["customer_acct_no"] = customer_acct_no
			break
		elif len(customer_acct_no) != 10:
			login_attempt -= 1
			print("\nwrong account number, you have ",login_attempt," trials left.\n")
		if login_attempt == 0:
			print("\nYou are out of trials!\nYou can't continue with the process, but you can try again later\n\n★**********★**********★**********★**********★\n\nYou are welcome to ABC Bank.\n\nPlease kindly follow the necessary procedure\n\n★**********★**********★**********★\n")
			#the login screen is displayed for the next user after unsuccessful verification
			login()
	#testing fir valid pin number
	while login_attempt > 0:
		customer_pin = input("\nYour pin number must be 5 digits long.\nEnter your pin number: ")
		while not customer_pin.isdigit():
			customer_pin = input("\nPlease enter a 5 digits number\nEnter your account number: ")
		if len(customer_pin) == 5:
			customers[customer_no]["customer_pin"] = customer_pin
			break
		elif len(customer_pin) != 5:
			login_attempt -= 1
			print("\nwrong account number, you have ",login_attempt," trials left.\n")
		if login_attempt == 0:
			print("\nYou are out of trials!\n\nYou can't continue with the process, but you can try again later\n\n★**********★**********★**********★\n\nYou are welcome to ABC Bank.\n\nPlease kindly follow the necessary procedure")
			#the login screen is displayed for the next user after unsuccessful verification
			login()
	#the main menu is displayed after sucessful verification
	main_menu()

customers = []	
customer_no = 0
customer_balance = 0

#The login function is called, this is the beginning if the code.
login()