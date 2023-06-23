#create a program that counts the number of times a character occurs in a sentence.
while 1:
	text = input("Enter any text: \n\t")
	count = {}
	for char in text:
		if not char in count:
			count[char] = 1
		else:
			count[char] += 1
	for char in count:
		print(" " +char +" - " + str(count[char]))
	#counting the number of words in the text entered
	print("There are "+str(count[" "] + 1)+ " words in text you entered.")