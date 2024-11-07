from pprint import pprint

class Human():

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def index_weight(self):
        imt = self.weight / (self.height ** 2)
        return round(imt, 2)

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = []
    for method in attributes:
        if callable(getattr(obj, method)):
            methods.append(method)
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info

number_info = introspection_info(42)
pprint(number_info)

class_info = introspection_info(Human(1.7, 60))
pprint(class_info)