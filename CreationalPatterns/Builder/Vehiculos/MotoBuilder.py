from Vehiculo import Vehiculo

class MotoBuilder(Vehiculo):
    
    def __init__(self):
        self.vehiculo = Vehiculo()
    
    def set_motor(self):
        self.vehiculo.motor = "2 tiempos - 150cc"
    
    def set_puertas(self):
        self.vehiculo.puertas = False
    
    def set_ruedas(self):
        self.vehiculo.ruedas = 2
    
    def set_aire_acondicionado(self):
        self.vehiculo.aire_acondicionado = False
    
    def get_vehiculo(self):
        return f"La moto consta de: \n - Motor: {self.vehiculo.motor}. \n - Ruedas: {self.vehiculo.ruedas}. \n - Puertas: {self.vehiculo.puertas}. \n - Tiene Aireacondicionado: {'Sí' if self.vehiculo.aire_acondicionado else 'No'}"