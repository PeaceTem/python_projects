#WAEC result report
record = []       

proceed = "yes"
position = 0

while proceed == "yes":
	#adding a student data to the record list
	record.append({})
	#adding students names
	student_name = input("What is your name?\n\t")
	record[position]["name"] = student_name
	#adding schools
	student_school = input("What is the name of your school? \n\t")
	record[position]["school"] = student_school
	#adding sessions
	student_session = input("Which session do you sit for O'level? ")
	record[position]["session"] = student_session
	#adding subjects taken and their scores
	record[position]["subjects"] = {}
	end_subject = "no"
	#creating a counter for the subjects
	subject_counter = 1
	while end_subject == "no":		
		subject = input("Enter a subject: ")
		letter = "What did you get in "+subject+"? "
		score = input(letter)
		#assigning score as the value of the key(subject)
		record[position]["subjects"][subject] = score
		#checking if subjects are up to 5
		if subject_counter >= 5:
			end_subject = input("Are these all the subjects? yes or no\n\t")
		else:
			end_subject = "no"	
			subject_counter += 1
	#checking if there are more students 
	proceed = input("Are there more students to be recorded? yes or no\n\t ")
	#the index number of the student data in the list(record)
	position += 1
#defining a function for grading the scores
def grade(mark):
	if mark >= 75 and mark <=100:
		return "A1"
	elif mark >= 70:
		return "B2"
	elif mark >= 65:
		return "B3"
	elif mark >= 60:
		return "C4"
	elif mark >= 55:
		return "C5"
	elif mark >= 50:
		return "C6"
	elif mark >= 45:
		return "D7"
	elif mark >= 40:
		return "E8"
	elif mark < 40 and mark >=0:
		return "F9"
	else:
		return None

for element in record:
	print("\nName :",element["name"],"\nSchool:",element["school"],"\nSession :",element["session"],"\nResult:\n")
	
	for key in element["subjects"]:
		print(key, ":", element["subjects"][key], " - ", grade(int(element["subjects"][key])), "\n\n")