def square(n):
    return n*n
numbers = [1,2,3,4]
result = map(square,numbers)
numbers_square = list(result)
print(numbers_square)

def muntiply(n):
    return n**n
numbers = (1,2,3,4)
output = map(muntiply,numbers)
numbers_muntiply = set(output)
print(numbers_muntiply)