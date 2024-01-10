# indexing starts from 0 in -ve slicing starts from -5 
list_a = [5,3,2,1,0]
part = list_a[-5:-2] # last index is not included 
print(part)

print('Negative Slicing')
print('The index -1 refers to the last element, -2 refers to the second-to-last element, and so on.')
text = "Hello, World!"
print(len(text))

# Using positive indices starts with 0 index 12! bot included 
positive_slice = text[7:12]
print("Positive slice:", positive_slice)  # Output: World

# Using negative indices
negative_slice = text[-6:-1]
print("Negative slice:", negative_slice)  # Output: World
