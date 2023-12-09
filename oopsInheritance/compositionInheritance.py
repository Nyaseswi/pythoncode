class GroceryItem:
    def __init__(self, name, regular_price, deal_price, weight):
        self.name = name
        self.regular_price = regular_price
        self.deal_price = deal_price
        self.weight = weight

    def get_deal_price(self):
        return self.deal_price

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Regular Price: {self.regular_price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"Weight: {self.weight} kg")

class ElectronicItem:
    def __init__(self, name, regular_price, deal_price, warranty):
        self.name = name
        self.regular_price = regular_price
        self.deal_price = deal_price
        self.warranty = warranty

    def get_deal_price(self):
        return self.deal_price

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Regular Price: {self.regular_price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"Warranty: {self.warranty} years")

class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print(f"Quantity: {quantity}")

    def display_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print(f"Total Bill: {total_bill}")

milk = GroceryItem("Milk", 40, 25, 3.5)
tv = ElectronicItem("TV", 45000, 40000, 3.5)
order = Order("Prime Delivery", "Hyderabad")
order.add_item(milk, 2) #add item medthod use chesi milk,tv are added to order 
order.add_item(tv, 1)
order.display_order_details()
order.display_total_bill()
