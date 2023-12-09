for i in range(2):
  print("Outer: " + str(i))
  for j in range(2):
    print(" Inner: " + str(j))
print("end of code ")
# 2nd example 
for i in range(1):
    print("outer:" + str(i))
    for j in range(0):
        print("outer:" + str(j))
i = 1 
total = 0 
while (i<3):
    j = 1
    while (j<3):
        if ((i**j)<6):
            total = total + 1
        j = j +1
    i = i +1
print(total)        

text1 = "program"
text2 = "code"
sum = 0
#common letter is o
for a in text1:
    for b in text2:
        if a ==b:
            sum = sum + 1 
print(sum)  

