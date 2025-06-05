from IBurgerBuilder import Burger, IBugerBuilder

class VeggieBurgerBuilder(IBugerBuilder):
    
    def __init__(self):
        self.burger = Burger()

    def add_bread(self):
        self.burger.bread = "Whole Wheat Bread"
    
    def add_meat(self):
        self.burger.meat = "Vegetable Meat"

    def add_cheese(self):
        self.burger.cheese = "Vegan cheese"
    
    def add_dressing(self):
        self.burger.dressing = "Avocato"
    
    def add_lettuce(self):
        self.burger.lettuce = True

    def add_tomato(self):
        self.burger.tomato = True

    def get_buger(self):
        return self.burger