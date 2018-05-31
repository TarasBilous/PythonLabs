from Dishes import *


class Cup(Dishes):

    def __init__(self, dishesType, material, volume, dishName):
        self.dishesType = dishesType
        self.material = material
        self.volume = volume
        self.dishName = dishName
