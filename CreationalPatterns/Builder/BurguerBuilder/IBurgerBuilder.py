from abc import ABC, abstractmethod

class Burger:
    def __init__(self):
        self.bread = ''
        self.meat = ''
        self.cheese = ''
        self.dressing = ''
        self.lettuce = False
        self.tomato = False

    def __str__(self):
        return f'Bread: {self.bread} | Meat: {self.meat} | Cheese: {self.cheese} | Dressing {self.dressing} | Lettuce: {self.dressing} | Tomato: {self.tomato}'
    


class IBugerBuilder(ABC):
    
    @abstractmethod
    def add_bread(self):
        pass
    
    @abstractmethod
    def add_meat(self):
        pass
    
    @abstractmethod
    def add_cheese(self):
        pass
    
    @abstractmethod
    def add_dressing(self):
        pass
    
    @abstractmethod
    def add_lettuce(self):
        pass
    
    @abstractmethod
    def add_tomato(self):
        pass
    
    #Remember that each burger must be returned to itself
    @abstractmethod
    def get_buger(self):
        pass