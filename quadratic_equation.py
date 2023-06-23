#Quadratic equation

print("This is a quadratic equation in form of\n\tax^2 + bx + c")
a = float(input("Enter a:  "))
b = float(input("Enter b:  "))
c = float(input("Enter c:  "))
d = b**2 - 4*a*c

if d == 0:
	print("The equation has two equal real roots.")
elif d > 0:
	print("The equation has two different real roots.")
elif d < 0:
	print("The equation has two complex roots.")
else:
	print("An error has occurred.")
	
x_1 =(-b + pow(d, 1/2))/(2*a)

x_2 =(-b - pow(d, 1/2))/(2*a)

print("The equation "+str(a)+"x^2 "+str(b)+"x "+str(c)+ " has the roots below.\nx_1 : "+str(x_1)+"\nx_2: "+str(x_2))
