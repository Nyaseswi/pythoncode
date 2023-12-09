from functools import reduce
def sum_of_num(a,b):
    return a +b 
numbers = [1,2,3,4]
sum_of_numbers = reduce(sum_of_num,numbers)
print(sum_of_numbers)