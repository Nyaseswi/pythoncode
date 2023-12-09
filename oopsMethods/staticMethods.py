class Cart:

   @staticmethod
   def greet():
       print("Have a Great Shopping")

Cart.greet()

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Calling a static method without creating an instance
result = MathOperations.add(5, 3)
print(result)  # Output: 8
