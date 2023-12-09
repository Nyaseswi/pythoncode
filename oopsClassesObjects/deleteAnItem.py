class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera = camera

    def remove_model(self):
        del self.model

# Create a Mobile object
mobile_object = Mobile("samsung", "64MP")
print(mobile_object.camera)

# Call the remove_model method to remove the 'model' attribute
mobile_object.remove_model()

# Now, if you try to print the object, you'll get an AttributeError
print(mobile_object)
