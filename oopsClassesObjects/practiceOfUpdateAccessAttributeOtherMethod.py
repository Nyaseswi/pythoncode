class Mobile:
    def __init__(self,model,camera):
        self.model = model 
        self.camera = camera
    def get_camera(self):
        print(self.camera)
    def make_call(self,number):
        print("calling..{}".format(number))
mobile_object = Mobile("samsung","64MP")
print(mobile_object.model) #access attribute with dot notation 
mobile_object.make_call(8919577668)  #make call function 
mobile_object.get_camera() #access attribute from other method 

#updating attributes 
class Shopping:
    def __init__(self,lehanga):
        
        self.lehanga = lehanga
    def update_leghanga(self,lehanga):
        self.lehanga = lehanga

Shopping_object = Shopping("blue_lehanga")
Shopping_object.update_leghanga("red_lehanga")
print(Shopping_object.lehanga)


