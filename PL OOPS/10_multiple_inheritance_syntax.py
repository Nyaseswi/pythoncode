#Inheritance - multiple inheritance syntax 
class Father:
    def fun1(self):
        print("This is Father class")
        print("--------------")
class Mother: 
    def fun2(self):
        print("This is Mother class")
        print("--------------")
class child(Father,Mother): #father mother idharini pettali
    def fun3(self):
        print("This is child class")
        print("--------------")
obj = child() #only child class ni matrame object tho call cheyali
 #print avthadi father mother class 
obj.fun1() 
obj.fun2()
obj.fun3()