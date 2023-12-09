print(id("Hello"))
a = "yaseswi"
print(id(a))
# finding id with concatenation 
a = "Hello"
print(id(a))
a = a +"World"
print(id(a))

a = 13
b = 17 
list_a = [5,7,11]
list_b = list_a
list_a = list_a + [a]
print(list_a)
list_a = [b]+list_a 
print(list_a)
print(id(list_a) == id(list_b))