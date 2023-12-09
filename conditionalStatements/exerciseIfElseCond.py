#1st example
age = 5
isEligible = (age >=18) and (age<=60)
if isEligible:
    print("Enjoy the ride")
else:
    print("Not eligible for the ride")
#2nd example
marks = 70 
if marks>85:
    print("A")
if marks>75:
    print("B")
if marks>50:
    print("C")
else:
    print("D")
#3rd example
a = 123
b = 124 
if a!=b:
    print("Not equal")
else:
    print("Equal")
#4th example
if not(False):
    print("True")
else:
    print("False")
#5th example
if 100==99:
    print("Same")
else:
    print("Not same")
#6th example   
a = (0.5 < 1.3) #True
b = (3 != 3) #False
if a and b: #False
    print(not(a and b)) #True
else:
    print(a or b) #False 
#7th example
length = 111
breadth = 111
if length != breadth:
    print("Rectangle")
else:
    print("Square")
#8th example
time = 15 
is_day = (time>=5) and (time<=18)
if is_day:
    print("Good morning,Keep smiling")
else:
    print("Good night")
#9th example
a =6
b = ((a*12)==32)
if b:
    print("True")
else:
    print("False")


