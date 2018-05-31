from Dishes import *


class Plate(Dishes):

    def __init__(self, dishesType, material, diameter, dishName):
        self.dishesType = dishesType
        self.material = material
        self.diameter = diameter
        self.dishName = dishName
