class Circle:
    min_bill =100
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

# Creating an instance and calling an instance method
circle = Circle(5)
area = circle.calculate_area()
print(area)  # Output: 78.53975

class Discount:
    def __init__(self,reduction):
        self.reduction = reduction
    def calculate_reduction(self):
        return 50*self.reduction**2
discount = Discount(5)
reduction = discount.calculate_reduction()
print(reduction)
