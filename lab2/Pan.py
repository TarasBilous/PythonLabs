from Dishes import *


class Color (Enum):
    WHITE = 1
    BLACK = 2
    RED = 3
    GRAY = 4


class Pan(Dishes):

    def __init__(self, dishesType, material, volume, cover, color, dishName):
        self.dishesType = dishesType
        self.material = material
        self.volume = volume
        self.cover = cover
        self.color = color
        self.dishName = dishName
