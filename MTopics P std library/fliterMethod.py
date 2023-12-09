def isPositive(num):
    return num>0
numbers = [1,-2,3,-4]
positive_numbers = filter(isPositive,numbers)
print(set(positive_numbers))
