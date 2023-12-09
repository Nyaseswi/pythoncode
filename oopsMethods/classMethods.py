class Cart:
   flat_discount = 0
   min_bill = 100
   @classmethod #decorator defined as class method 
   def update_flat_discount(cls,  
                          new_flat_discount): #cls as argument 
       cls.flat_discount = new_flat_discount # Cart.ani call chesinattu 

Cart.update_flat_discount(25)
print(Cart.flat_discount)

#example 
class User:
    name = "yaseswi"
    age = 25 
    @classmethod
    def update_name(cls,new_name):
        cls.name = new_name
User.update_name("Namala Venkata Yaseswi")
print(User.name)