message = "Hello yaseswi"
part = message[6:13]
print(part)  # This will output " yaseswi"
part = message[6:]
print(part)

name = 'Hello yaseswi'
print(len(name))
part0 = "Reads the entire string:",name[0:]
part1 = "Last index is not included:", name[0:4]
part2 = "Reads 1st index even if not included:",name[:13]
print(part0)
print(part1)
print(part2)
