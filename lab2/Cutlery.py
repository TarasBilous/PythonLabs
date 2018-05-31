from Dishes import *


class CutleryType (Enum):
    FORK = 1
    KNIFE = 2
    SPOON = 3


class Cutlery(Dishes):

    def __init__(self, dishesType, material, cutleryType, dishName):
        self.dishesType = dishesType
        self.material = material
        self.cutleryType = cutleryType
        self.dishName = dishName
