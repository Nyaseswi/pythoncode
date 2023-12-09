#single inheritance 
class parent:
    def fun1(self):
        print("This is parent class")
class child(parent): #inherit cheseapudu parent lo class name pettali
    def fun2(self):
        print("This is child class")
obj = child() #only child class ni matrame object tho call cheyali
obj.fun2() #print avthadi 
obj.fun1() 

#example 
class Mobile():
    def brands(self):
        
        print("This is brand section")
        
class Prices(Mobile):
    def prices(self):
        print("This is price section")
        
obj = Prices()
obj.brands()
obj.prices()
        