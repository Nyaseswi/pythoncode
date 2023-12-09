class Mobile:
    def __init__(self,model,camera): #Mobile ane class ki property define chesa 
        self.model = model
        self.camera = camera
    def display(self): #display function create chesa 
        print("Model:",self.model) #self. pettali lekapothe name error ani vasthundi 
        print("Camera:",self.camera)
mobile_object1 = Mobile("Samsung","64MP") #values pass chesa properties model camera ki
mobile_object2 = Mobile("Nokia","4MP")
mobile_object1.display() 
mobile_object2.display()#display function call chesa
