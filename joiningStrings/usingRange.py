list_a = list(range(4))
print(list_a)
# i want to add comma or the above list 
joined_string = ','.join(list_a)
print(joined_string) # we get type eror because we cant add/join comma for range elements 
# we can add only for string elements sequece 
