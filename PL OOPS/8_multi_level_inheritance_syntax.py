#Inheritance - multi level inheritance syntax 
class parent:
    def fun1(self):
        print("This is parent class")
        print("--------------")
class child(parent): #inherit cheseapudu parent lo class name pettali
    def fun2(self):
        print("This is child class")
        print("--------------")
class grandchild(child): #inherit cheseapudu parent lo class name pettali
    def fun3(self):
        print("This is grandchild class")
        print("--------------")
obj = grandchild() #only grandchild class ni matrame object tho call cheyali
 #print avthadi parent child class 
obj.fun1() 
obj.fun2()
obj.fun3()