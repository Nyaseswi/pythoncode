class discount:
    min_dis = 50
    max_dis = 100
    def print_max_bill(self):
        print(discount.max_dis)
a = discount()
b = discount()
discount.max_dis = 200 #value remains same 
print(a.max_dis) 
print(b.max_dis)