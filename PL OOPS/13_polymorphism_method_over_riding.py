class A:
    def display(self):
        print("This is class A")

class B(A):  # Inheriting from class A
    def display(self):
        print("This is class B")
        super().display()

obj = B()
obj.display()
