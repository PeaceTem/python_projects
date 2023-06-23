print("Welcome!")
customer_acct_no = int(input("Enter your account number: "))

while  len(str(customer_acct_no)) != 10:
	customer_acct_no = int(input("Enter your account number: "))
customer_pin = int(input("Enter your pin number: "))
while len(str(customer_pin)) != 5:
	customer_pin = int(input("Enter your pin number: "))

print(customer_acct_no," ", customer_pin)
print("Main Menu:\n\t1. View my Account\n\t2. Withdraw cash\n\t3. Deposit  funds\n\t4. Exit")
choice1 = int(input("Enter your choice: \n\t"))
if choice == 1:
	print("This should output the account balance")
elif choice == 2:
	#create the withdrawal function
elif choice == 3:
	#create the deposition function
elif choice == 4:
	#use the exit function



