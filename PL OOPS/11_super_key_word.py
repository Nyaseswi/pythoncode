#super keyword 
class A: #Class A and class B
    def __init__(self): #Class A lo init class B lo init 
        print("This is class a")
    def fun1(self):
        print("This is Father class")
class B(A): #Class B ni A tho inherit chesa , inherit chesthe class A lo unna properties class B loki ravali 
    def __init__(self):
        print("This is class b")
        super().__init__() #super keyword pedithe a lo unna properties kuda call avthayi
    def fun1(self):
        print("This is Mother class")
obj=B() #b okate vasthadi 
    