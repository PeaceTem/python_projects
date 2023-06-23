#This is a counpoind calculator
#ít takes in complex operationsand prints out the result.
import math
#addition function
def add( n, m):
	return n + m
	
#subtraction function
def sub( n, m):
	return n - m
	
#multiplication function	
def mult(n, m):
	return n * m
	
#division function
def div(n, m):
	return n / m
	
operation = input("Enter the operation you want to perform:  ")

for elem in operation:
	