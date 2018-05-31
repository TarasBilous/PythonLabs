from Dishes import *


class FryingPan(Dishes):

    def __init__(self, dishesType, material, volume, cover, dishName):
        self.dishesType = dishesType
        self.material = material
        self.volume = volume
        self.cover = cover
        self.dishName = dishName
