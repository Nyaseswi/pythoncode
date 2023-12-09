#1st example
list_a = [True, True]
is_all_true = all(list_a)

print(is_all_true) #returns true 
#2nd example
set_a = {}
is_all_true = all(set_a)

print(is_all_true) #returns true 
#3rd example
is_true_in_list = all([1, 5, 0, 4])
is_true_in_set = all({True, "Teja", 7})
is_true_in_tuple = all(("", "hello", "world"))

print(is_true_in_list)#returns False 
print(is_true_in_set)#returns true 
print(is_true_in_tuple)#returns False 

#4th example 
dict_a = {
  "name": "Teja",
  "age": 15
}

is_all_true = all(dict_a)
print(is_all_true) #returns true 

#5th example
dict_a = {
  0: "Hello",
  1: "World"
}

is_all_true = all(dict_a)
print(is_all_true) #returns False 