#list concatenation
a = 2 
list_a = ["six", 6 , 66.10, True, a]
list_b = [1, 1.0, "one", False, list_a]
result = list_a + list_b
print(result)
#concatenation 2nd example 
wild_animals = ['tiger','lion']
domestic_animals = ['cat','dog']
animals = wild_animals + domestic_animals
animals1 = [wild_animals] + [domestic_animals]
print(animals)
print(animals1)
#list repetition 
a = 2 
list_a = ["six", 6 , 66.10, True, a]
list_b = [1, 1.0, "one", False, list_a]
result = list_a * 3
print(result)
#listSlicing
a = 2 
list_a = ["six", 6 , 66.10, True, a]
list_b = [1, 1.0, "one", False, list_a]
result = list_a[0:2]
print(result)
