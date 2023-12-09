
# def and calling a function
def sayHi():
    print("hello world")
sayHi()

# passing value as argument 
def sayHi(word):
    msg = "Hello " + word 
    print(msg)
sayHi(word = "World!")

#return function 
def sayHi(word):
    msg = "Hello " + word
    return msg 
greet= sayHi(word="World!")
print(greet)