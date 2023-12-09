class Cart:
    def __init__(self,grocery,clothes):
        self.grocery = grocery
        self.clothes = clothes
    def add_cart(self,text):
        print("Buy Women Clothing Online in India{}".format(text))

mobile_obj = Cart("samsung","64MP")  
mobile_obj.add_cart(" Added to cart")
        