dict_a = {
    'name': 'Yaseswi',
    'roll_no': 'Y16phd0829',
    'city': 'Vijayawada',
    'Job':'Medical Scribe',
    'company':'Aquity Solutions'
}
dict_b = dict_a
dict_b['city'] = 'vizag'
print(dict_b)
#refer same object with same id number 
print(id(dict_a))
print(id(dict_b))