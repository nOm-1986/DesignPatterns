class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self):
        return "Hello " + self.name
    
    def show_age(self):
        return self.age
    
    def is_of_legal_age(self):
        if self.age >= 18:
            return True
        return False