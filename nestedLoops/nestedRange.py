count = 0 
for i in range(4):
    for j in range(2,5):
        if i>j:
            count = count + 1
print(count)

result = 1 
for i in range(5,7):
    for j in range(5,7):
        if i%j !=0:
            result = result + 1 
print(result)

result = 1 
for i in range(5,7):
    for j in range(5,7):
        if i%j !=0:
            result = result + 1 
print(result)
result = 10 
for i in range(3):
    for j in range(i):
        result = result - 2
        print(result)
for i in range(1,3):
    for j in range(1,4):
        if (i==j):
            print("Square of " + str(i) + " is " + str(i*i))
for i in range(0,1):
    for j in range(2,3):
        print("Super")