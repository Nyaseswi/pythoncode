class Mobile:
    def __init__(self,model):
        self.model = model 
        
    def make_call(number):
        print("calling..{}".format(number))
    def update_model(self,model): #create new model 
        self.model = model
mobile_object = Mobile("Samsung")
mobile_object.update_model("Nokia") #define update model  var.fun_name("updated_name")
print(mobile_object.model) #print  var.property
