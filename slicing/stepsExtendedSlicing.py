a = "Waterfall"
part = a[0:13:2]
print(part)

slicingName = "Steps Slicing"
print(slicingName)
name = 'Namala Venkata Yaseswi'
print(len(name))
part0 = name[:22:2]
part1 = name[:22:3]
part2 = name[:22:4]
print("2 steps means leaves one word",part0)
print("3 steps means leaves 2 words",part1)
print("4 steps means leaves 3 words",part2)

// revision:
name = 'Namala Venkata Yaseswi '
print('Reads the entire string:',name[0:])
print('Last index is not included:', name[0:5])
print('Reads start index even if left empty:', name[:6])
print('2 step extended slicing:', name[0:6:2])
print('3 step extended slicing:', name[0:6:3])
print('4 step extended slicing:', name[0:6:4])
print('-1 last element:', name[-8:-1])
print('Reverse String:', name[::-1])

