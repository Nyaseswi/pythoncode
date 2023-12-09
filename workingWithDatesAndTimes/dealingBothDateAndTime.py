from datetime import datetime
datetime_object = datetime(2023,11,10,15,3,2)
print(datetime_object.year)
print(datetime_object.month)
print(datetime_object.hour)
print(datetime_object.minute)

#current time 
current_time_object = datetime.now()
print(current_time_object)
print(current_time_object.year)