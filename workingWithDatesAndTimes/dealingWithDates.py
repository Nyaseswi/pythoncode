import datetime 
#date class year month day
date_object = datetime.date(2023,11,20)
print(date_object)
#Access attributes from datetime 
print(date_object.year)
print(date_object.month)
print(date_object.day)
#today method in datetime 
date_object = datetime.date.today()
print(date_object)

