#Esta es nuestra clase base --- Seria bueno definirla abstracta
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None
    
    def __str__(self):
        return f'Dough: {self.dough} | Sauce: {self.sauce} | Topping: {self.topping}'