from pizza import Pizza

class PizzaBuilder:
    def set_dough(self, dough):
        pass

    def set_sauce(self, sauce):
        pass

    def set_topping(self, topping):
        pass

class MargueritaBuilder(PizzaBuilder):
    def __init__(self):
        self._pizza = Pizza()

    def set_dough(self):
        self._pizza.dough = "Regular"
    
    def set_sauce(self):
        self._pizza.sauce = "Tomato"

    def set_topping(self):
        self._pizza.topping = "Mozarrella"
