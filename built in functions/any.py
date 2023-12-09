list_a = [True, False]
is_any_true = any(list_a)

print(is_any_true) #returns true

set_a = {}
is_any_true = any(set_a)

print(is_any_true) #returns False 

is_true_in_list = any([0, 0, 2, 0])
is_true_in_set = any({"", None, 0})
is_true_in_tuple = any(("hello", "world"))

print(is_true_in_list) #returns true
print(is_true_in_set) #returns False 
print(is_true_in_tuple)#returns true

dict_a = {
  0: "Teja",
  1: 15
}

is_any_true = any(dict_a)
print(is_any_true) #returns true

dict_a = {
  0: "hello",
  False: "world"
}

is_any_true = any(dict_a)
print(is_any_true)#returns False 