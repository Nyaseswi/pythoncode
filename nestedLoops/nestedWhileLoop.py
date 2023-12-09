outer_count = 1
while outer_count <= 3:  # Outer loop runs 3 times
    inner_count = 1
    while inner_count <= 3:  # Inner loop runs 3 times for each outer loop iteration
        print("Outer:", outer_count, "Inner:", inner_count)
        inner_count += 1  # Increment inner_count
    outer_count += 1  # Increment outer_count
count = 0 
for i in range(1,3):
    for j in range(1,3):
        if i%j == 0:
            count = count + 1 
            print(count)         
total = 0 
for i in range(3):
    for j in range(3,6):
        if i ==j:
            total = total + 2 
            print(total)
print(total)