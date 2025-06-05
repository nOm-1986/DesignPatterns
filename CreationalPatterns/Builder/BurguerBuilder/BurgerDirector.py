from IBurgerBuilder import IBugerBuilder

class BurgerDirector:
    def make_burger(self, burger_builder: IBugerBuilder):
        burger_builder.add_bread()
        burger_builder.add_meat()
        burger_builder.add_cheese()
        burger_builder.add_lettuce()
        burger_builder.add_tomato()
        burger_builder.add_dressing()
    