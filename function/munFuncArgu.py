def greet(arg_1 , arg_2):
    print(arg_1 + " " + arg_2)
greeting = "Good morning" 
name = "ram"
greet(arg_1= greeting, arg_2=name) #order value not matters in sequence 
#positional arguments 
def greet(arg_1 , arg_2):
    print(arg_1 + " " + arg_2)
greeting = "Good morning" 
name = "ram"
greet( greeting, name)
greet(name,greeting) #order value matters in sequence  
