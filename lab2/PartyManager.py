class PartyManager:
    dishes = []

    def __init__(self):
        pass

    def sort_by_material(self):
        self.dishes.sort(key=lambda dishes: dishes.material)

    def find_by_dishName(self, *dishNames):
        founded_dishes = []
        for dishName in dishNames:
            for dishes in self.dishes:
                if dishes.dishName == dishName:
                    founded_dishes.append(dishes)

        return founded_dishes

    def add_dishes(self, dishes):
        self.dishes += dishes

    def print_list(self):
        for dishes in self.dishes:
            print(dishes)
        print()
