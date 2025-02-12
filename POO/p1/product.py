class Product:
    
    def __init__(self,id: int, name: str, valor: int):
        self.__id = id #Private attribute
        self.__name = name # Protected attribute
        self.__price = valor

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def price(self) -> int:
        return self.__price
    
    @price.setter
    def price(self, valor: int):
        self.__price = valor

    def calculate_total(self, amount: int) -> int:
        return amount * self.__price

    #ToString del objeto
    def __str__(self):
        return f"Information about your product: ID {self.__id}, Name: {self.__name}, Price: {self.__price}"
    

p1 = Product(1, "Orthopedic Mattress",  500)
print(p1.calculate_total(20))
