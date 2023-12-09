class Mobile:
    def __init__(self,model,camera,):
        self.model= model
        self.camera=camera
    def make_call(self,number):
        print("calling...{}".format(number))
#The above is blueprint 
mobile_obj = Mobile("samsung","64MP") #edi define cheyali mobile_obj ni class tho define chesi call cheyali
mobile_obj.make_call(8919577668)
# print(mobile_obj)
print(type(mobile_obj))