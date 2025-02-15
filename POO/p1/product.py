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
        self.__name = name
    
    @property
    def price(self) -> int:
        return self.__price
    
    @price.setter
    def price(self, valor: int):
        if valor > 0:
            self.__price = valor
        else:
            raise ValueError('Price can not be less than one mf...')

    def calculate_total(self, amount: int) -> int:
        return amount * self.__price

    #ToString del objeto
    def __str__(self):
        return f"Information about your product: ID {self.__id}, Name: {self.__name}, Price: {self.__price}"


class Pedido:
    def __init__(self):
        self.__products = []
        self.__cuantity = []
    
    def total_pedido(self):
        total = 0
        for (p, c) in zip(self.__products, self.__cuantity):
            total += p.calculate_total(c)
        return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__products, self.__cuantity):
            print(f"Producto: {p.name}, valor: {p.price}. cantidad {c}")
    
    #def add_produc(self, product: Product, cuantity: int): Esta es la forma correcta utilizada actualmente por seguir el curso utilizo la antigua
    def add_produc(self, product: Product, cuantity: int):
        if not isinstance(product, Product):
            raise Exception('Product must be a Product type')
        if cuantity <= 0:
            raise Exception('Cuantity must be a positive value')
        if product in self.__products:
            indice = self.__products.index(product)
            self.__cuantity[indice] += cuantity
        else:
            self.__products.append(product)
            self.__cuantity.append(cuantity)
    
    def delete_product(self, product: Product):
        if product in self.__products:
            indice = self.__products.index(product)
            del self.__products[indice]
            del self.__cuantity[indice]
        else:
            raise Exception("Your product does not exits")

    

if __name__ == "__main__":
    p1 = Product(1, "Orthopedic Mattress",  500)
    p2 = Product(2, "Pillow",  25)
    p3 = Product(3, "Basement bed",  80)
    produc_list = [p1, p2, p3]
    cuantity = [2,4,6]
    #pedido1 = Pedido(produc_list, cuantity)
    try:
        pedido1 = Pedido()
        pedido1.add_produc(p1, 5)
        pedido1.add_produc(p2, 5)
        pedido1.add_produc(p3, 5)
        total = pedido1.total_pedido()
        print(total)

    except Exception as e:
        print(e)
