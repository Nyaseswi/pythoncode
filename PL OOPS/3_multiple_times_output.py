class Mobile:
    def __init__(self,model,camera): #Mobile ane class ki property define chesa 
        self.model = model
        self.camera = camera
    def display(self): #display function create chesa 
        print("Model:",self.model) #self. pettali lekapothe name error ani vasthundi 
        print("Camera:",self.camera)
for i in range(4): #4 times iterate 
    mobile_object = Mobile("Samsung","64MP") #values pass chesa properties model camera ki
    mobile_object.display() #display function call chesa
