#weather conditions
#data
weather = [
	{
	 "regionId" : "SW01"  ,
	"state" : "Oyo" ,
	"temp" :23.8 ,
	"rainfall" : 5.2 ,
	"pressure" : 3.0
	},
	{
	 "regionId" :  "SW02" ,
	"state" : "Ogun",
	"temp" :28.5,
	"rainfall" : 6.8 ,
	"pressure" : 5.9
	},
	{
	 "regionId" :  "SW03" ,
	"state" : "Lagos" ,
	"temp" : 20.5,
	"rainfall" : 12.7 ,
	"pressure" : 4.6
	},
	{
	 "regionId" : "SW04"  ,
	"state" : "Ondo" ,
	"temp" : 23.7 ,
	"rainfall" : 10.6,
	"pressure" : 2.8
	},
	{
	 "regionId" : "SW05"  ,
	"state" : "Ekiti",
	"temp" : 26.6,
	"rainfall" :7.8 ,
	"pressure" : 2.9
	}
]

# mean function
def get_mean(column):
	total = 0
	for element in weather:
		total += element[column]	
	mean = total/len(weather)
	return mean

# function fir getting R
def get_R(x,y):
	x_mean = get_mean(x)
	y_mean = get_mean(y)
	summation = 0
	for row in weather:
		summation +=(((row[x] - x_mean)**2) * ((row[y] - y_mean)**2))
	r_value = summation/(summation**0.5)
	return r_value

print("The R value for the temperature and rainfall is :")			
print(get_R("temp", "rainfall"))

weather[0]["temp"] = 3
weather[1]["temp"] = 1
weather[2]["temp"] = 2
weather[3]["temp"] = 3
weather[4]["temp"] = 1

weather[0]["rainfall"] = 5.2
weather[1]["rainfall"] = 6.8
weather[2]["rainfall"] = 12.7
weather[3]["rainfall"] = 10.6
weather[4]["rainfall"] = 7.8


print("The R value for the temperature and rainfall is :")
print(get_R("temp", "rainfall"))


