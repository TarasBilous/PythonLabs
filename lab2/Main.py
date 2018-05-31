from Plate import *
from FryingPan import*
from Pan import *
from Cup import *
from Cutlery import *
from PartyManager import *

manager = PartyManager()

plate = Plate(DishesType.KITCHENWARE, Material.CERAMICS, 0.5, "plate")
fryingPan = FryingPan(DishesType.TABLEWARE, Material.METAL, 2.5, True, "fryingPan")
pan = Pan(DishesType.TABLEWARE, Material.PORCELAIN, 20.3, True, Color.GRAY, "pan")
cup = Cup(DishesType.KITCHENWARE, Material.GLASS, 20.4, "cup")
knife = Cutlery(DishesType.KITCHENWARE, Material.GLASS, CutleryType.KNIFE, "knife")
manager.dishes = [plate, fryingPan, pan, cup, knife]

manager.sort_by_material()
manager.print_list()

manager.dishes = manager.find_by_dishName("pan", "knife")
manager.print_list()