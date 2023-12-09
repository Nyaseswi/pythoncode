dict_a = {
    'name': 'Yaseswi',
    'roll_no': 'Y16phd0829',
    'city': 'Vijayawada',
    'Job':'Medical Scribe',
    'company':'Aquity Solutions'
}
dict_a_copy = dict_a.copy() #copy with a new variable name 
print(dict_a_copy)
print(dict_a)

#copy method differs different id of dict objects 
print(id(dict_a_copy))
print(id(dict_a))