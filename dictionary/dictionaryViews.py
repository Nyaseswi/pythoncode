dict_a = {
    'name':'Rubysmitha',
    'Roll no':'Y16phd0830',
    'age': 28,
}
print(dict_a.keys())#getting keys 
print(dict_a.values())#getting values
print(dict_a.items())#getting both keys & values 

#iterating on keys,values, items 
for keys in dict_a:
    print(keys)

for values in dict_a.values():
    print(values)

for items in dict_a.items():
    print(items)

#Converting to dict type 
print(type(dict_a))
list_a = [('name','Teja'), ['age',15],

('city','Hyderabad')
]
dict_a = dict(list_a)
print(dict_a)