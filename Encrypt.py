# data encryption
given_string = input("Enter a word or sentence to be encrypted: ")
#function to reverse string
def reverse_string(string):
	reversed_string = ""
	for letter in string:
		reversed_string =  letter + reversed_string
		
	return reversed_string
	
#the vowel equivalent
vowels_value = {
"a" : "1",
"e" : "5",
"i" : "3",
"o" : "2",
"u" : "4"
}
# getting the key of a dictionary value
def get_key(val, mydict):
	for key, value in mydict.items():
		if val == value:
			return key
			
#encrytion function
def encrypt(string):
	while len(string) < 10:
		string = input("Enter a new string: ")
		
	string_A = string[ : (len(string)//2)]
	string_B = string[((len(string)//2)) : ]
	reversed_string_A = reverse_string(string_A)
	reversed_string_B = reverse_string(string_B)
	final_string = reversed_string_B + reversed_string_A
	string_list = []
	for letter in final_string:
		if letter in vowels_value.keys():
			string_list.append(vowels_value[letter])
		else:
			string_list.append(letter)
	
	final_string = ""
	for item in string_list:
		final_string += item
		
	return final_string
		
#decryption function
def decrypt(string):
	if len(string) % 2 != 0:
		reversed_string_B = string[ : (len(string)//2 + 1)]
		reversed_string_A = string[(len(string)//2 + 1) : ]
	else:
		reversed_string_B = string[ : (len(string)//2)]
		reversed_string_A= string[(len(string)//2 ) : ]
		
	string_A = reverse_string(reversed_string_A)
	string_B = reverse_string(reversed_string_B)
	final_string = string_A + string_B

	string_list = []
	for letter in final_string:
		if letter in vowels_value.values():
			string_list.append(get_key(letter, vowels_value))
		else:
			string_list.append(letter)
	
	final_string = ""
	for item in string_list:
		final_string += item
		
	return final_string

encrypted_string = encrypt(given_string)
decrypted_string = decrypt(encrypted_string)
print("The given string is:", given_string)
print("\nThe encrypted string is:", encrypted_string)
print("\nThe decrypted string is:", decrypted_string)