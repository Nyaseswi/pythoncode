#square brackets 
dict_a = {
    'name':'Yaseswi',
    'age':25,
    'study':'Pharm D',
}
print(dict_a['name'])
#print(dict_a['city']) #keyError

#getOf method 
dict_a = {
    'name':'Yaseswi',
    'age':25,
    'study':'Pharm D',
}
print(dict_a.get('name'))
print(dict_a.get('city')) #None 
