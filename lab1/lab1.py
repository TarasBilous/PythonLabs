class Farm:
    totalFieldSquare = 0

    def __init__(self, name="default", price=0, fieldSquare=0, plantKind="default", country="default"):
        self._name = name
        self.price = price
        self.fieldSquare = fieldSquare
        self.plantKind = plantKind
        self.country = country
        Farm.totalFieldSquare += fieldSquare

    def to_string(self):
        print("Name: " + self.name + "; Price:", self.price,
              "; FieldSquare:", self.fieldSquare, "; PlantKind:" + self.plantKind + "; Country:", self.country, ";")

    def print_sum(self):
        print("FieldSquare " + self.name + ": ", self.fieldSquare)

    @staticmethod
    def print_static_sum():
        print("TotalFieldSquare: ", Farm.totalFieldSquare)


if __name__ == '__main__':
    vladFarm = Farm("Vlad farm", 42000, 200, "corn", "England")
    tomFarm = Farm()
    andrewFarm = Farm("Andrew farm", 56000, 400, "wheat")

    print("\n")
    vladFarm.to_string()
    tomFarm.to_string()
    andrewFarm.to_string()

    print("\n")
    vladFarm.print_sum()
    tomFarm.print_sum()
    andrewFarm.print_sum()

    print("\n")
    Farm.print_static_sum()
