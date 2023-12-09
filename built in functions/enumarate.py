name = "Teja"
enumerate_name = enumerate(name)

print(list(enumerate_name))

set_a = {1, 2, 3, 4}

enumerate_set = list(enumerate(set_a, 10))
print(enumerate_set)

#Looping over enumarate 
names = ["Jack", "John", "James"]

for each_name in enumerate(names):
    print(each_name)

names = ["Jack", "John", "James"]

for count, each_name in enumerate(names):
    tuple_a = (count, each_name)
    print(tuple_a)