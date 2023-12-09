class Mobile:
    def __init__(self, model, camera):
        self.model = model  # Use '=' instead of ':'
        self.camera = camera  # Use '=' instead of ':'

    def make_call(self, number):
        print("calling...{}".format(number))

mobile_obj1 = Mobile("Galaxy M51", "64MP")
mobile_obj2 = Mobile("iphone 12 pro", "12MP")
print(mobile_obj2.camera) #access attributes with dot notation print(var.property)