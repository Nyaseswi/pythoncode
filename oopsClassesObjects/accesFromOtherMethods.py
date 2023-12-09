class Mobile:
    def __init__(self,model,camera):
        self.model = model
        self.camera = camera
    def get_model(self):
        print(self.model)
    def make_call(number):
        print("calling..{}".format(number))
mobile_object = Mobile("Samsung","64MP")
print(mobile_object.get_model())
mobile_object.get_model() #to not to get none  var.method_name
 
