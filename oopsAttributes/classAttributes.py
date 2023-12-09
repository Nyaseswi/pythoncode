class Dog:
    species = "Canis familiaris"  # Class attribute

# Accessing a class attribute
print(Dog.species)  # Output: "Canis familiaris"

class Dog:
    def __init__(self,species): 
        self.species = species
dog_object = Dog("Canis familiaris")
print(dog_object.species)# Accessing a class attribute
