list_a = [1, 2, 3, 4]
list_b = list_a.copy()
print(list_b)

list_a = ["a", "b", "c"]
list_b = list_a
list_a[0] = "z"
print(list_b)


list_1 = ["a", "b", "c"]
list_2 = list_1.copy()
list_1[0] = "z"
print(list_2)

list_a = ["a", "b", "c"]
list_b = [1, 2, 3, list_a]

list_c = list_b.copy()
list_a[0] = "z"

print(list_c)