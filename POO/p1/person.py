class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age

    def greeting(self):
        return "Hello " + self._name
    
    def show_age(self):
        return self.age
    
    def is_of_legal_age(self):
        if self.age >= 18:
            return True
        return False

    #Setters and Getters
    """
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    Forma Pro de hacer Getters y Setters
    @property
    """
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def get_age(self):
        return self.age
    
    def set_age(self, age: int):
        if type(age) == int:
            self.age = age
        else:
            raise ValueError('Please, Put a #$#@$%^@ number')