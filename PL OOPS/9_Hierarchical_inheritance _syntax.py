#Inheritance - Hierarchical inheritance syntax 
class parent:
    def fun1(self):
        print("This is parent class")
        print("--------------")
class child1(parent): #inherit cheseapudu parent lo class name pettali
    def fun2(self):
        print("This is child class")
        print("--------------")
class child2(parent): #inherit cheseapudu parent lo class name pettali
    def fun3(self):
        print("This is grandchild class")
        print("--------------")
obj1 = child1()  # Create an instance of child1
obj1.fun1()
obj1.fun2()  # Call the fun2 method on obj1

obj2 = child2()  # Create an instance of child2
# obj2.fun1()
obj2.fun3()

