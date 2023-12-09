class Cart:
    count = 0 
    min_bill= 100
    def __init__(self,clothes,groceries):
        self.clothes = clothes
        self.groceries = groceries
cart_object = Cart("punjabi","dalchawal")
print(cart_object.clothes)
print(Cart.min_bill) #using class method we can directly access attribute 
#access within methods 



