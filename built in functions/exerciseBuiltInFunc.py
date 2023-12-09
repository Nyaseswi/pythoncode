#want to separate digits from input and arrange in list 
#digist_list is variable name and passed empty list here 
#input meda iterate ayyi digits ni extract cheyali 
#isdigit ayithe int datatype lo concert chesi list lo ivvali
str_1 = input()

digits_list = [] 
for char in str_1:
    if char.isdigit():
        digits_list += [int(char)]
        print(digits_list)

#sum_of_numbers 
sum_of_numbers = sum(digits_list)
print(sum_of_numbers)

#min
min_of_numbers = min(digits_list)
print(min_of_numbers)
#max
max_of_numbers = max(digits_list)
print(max_of_numbers)


#we can also write this as funtion 

 
