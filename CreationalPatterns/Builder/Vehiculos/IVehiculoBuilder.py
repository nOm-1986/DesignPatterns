from abc import ABC, abstractmethod


class IVehiculosBuilder(ABC):
    
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
    