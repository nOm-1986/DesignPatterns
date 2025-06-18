from abc import ABC, abstractmethod
from Vehiculo import Vehiculo

class IVehiculosBuilder(ABC):
    def __init__(self):
        self.vehiculo = Vehiculo()
    
    @abstractmethod
    def set_motor(self):
        pass
    
    @abstractmethod
    def set_ruedas(self):
        pass

    @abstractmethod
    def set_puertas(self):
        pass

    @abstractmethod
    def set_aire_acondicionado(self):
        pass
    
    @abstractmethod
    def get_vehiculo(self):
        pass
    