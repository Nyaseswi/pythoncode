def greet(arg1="Hi", arg2="Ram"):
    print(arg1 + " " + arg2)

data = ["Hello", "Teja"] #list type 
greet(*data)

#dictionary type 
def greet(arg1="Hi", arg2="Ram"):
    print(arg1 + " " + arg2)

data = {'arg1':'Hello', 'arg2':'Teja'}
greet(**data)