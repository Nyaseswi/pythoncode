class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating instances of the class with unique attributes
dog1 = Dog("Buddy", 3)
dog2 = Dog("Molly", 5)

# Accessing instance attributes
print(dog1.name) 
print(dog1.age)# Output: "Buddy"
print(dog2.name)
print(dog2.age)   # Output: 5

class Mobile:
    def __init__(self,model,camera):
        self.model = model
        self.camera = camera
mobile1 = Mobile("samsung", 64)
mobile2 = Mobile("Nokia",36)

print(mobile1.model)
print(mobile2.camera)


