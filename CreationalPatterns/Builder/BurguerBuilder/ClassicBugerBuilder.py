from IBurgerBuilder import IBugerBuilder, Burger

class ClassicBurgerBuilder(IBugerBuilder):
    
    def __init__(self):
        self.burger = Burger()
    
    def add_bread(self):
        self.burger.bread = "Sesame bread"

    def add_meat(self):
        self.burger.meat = "Broasted meat"
    
    def add_cheese(self):
        self.burger.cheese = "Cheddar cheese"
    
    def add_dressing(self):
        self.burger.dressing = "Ketchup"

    def add_lettuce(self):
        self.burger.lettuce = False
    
    def add_tomato(self):
        self.burger.tomato = True

    def get_buger(self):
        return self.burger