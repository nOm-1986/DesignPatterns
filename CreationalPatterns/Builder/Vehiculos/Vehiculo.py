class Vehiculo:
    
    def __init__(self):
        self.motor: str = None
        self.ruedas: int = 0
        self.puertas: bool = False
        self.aire_acondicionado: bool = False
    
    def __str__(self):
        return f"El vehículo consta de: \n - Motor: {self.motor}. \n - Ruedas: {self.ruedas}. \n - Puertas: {self.puertas}. \n - Tiene Aireacondicionado: {'Sí' if self.aire_acondicionado else 'No'}"