#clear
set_a = {1,2,3,4,5,6}
set_a.clear()
print(set_a)
#length
set_a = {1,2,3,4,5,6}
print(len(set_a))
#iterating
set_a = {1,2,3,4,5,6}
for item in set_a:
    print(item)
#Membership check 
set_a = {1,2,3,4,5,6}
is_part_a = 11 in set_a
is_part_b = 2 not in set_a
print(is_part_a)
print(is_part_b)