#1st example
points = float(45.3)
if points>80:
    print("Very good")
elif points>60:
    print("good")
else:
    print("Better luck next time")
#2nd example
pollution_percentage = float(80.5)
if pollution_percentage >95:
    print("pollution level is very high")
elif (pollution_percentage>75) and pollution_percentage <=95:
    print("pollution level is moderate") 
else:
    print("pollution level is insignificant") 
#3rd example
a = 43
b = 67
if a>b:
    a = a +3 
elif (a==b):
    a = a+4
else:
    a = a+5
    print(a)