from IVehiculoBuilder import IVehiculosBuilder

class CamionBuilder(IVehiculosBuilder):
    
    

    def set_motor(self):
        self.vehiculo.motor = "4000 cc - Diesel"
    
    def set_puertas(self):
        self.vehiculo.puertas = 2
    
    def set_ruedas(self):
        self.vehiculo.ruedas = 4
    
    def set_aire_acondicionado(self):
        self.vehiculo.aire_acondicionado = True
    
    def get_vehiculo(self):
        return f"El Camión consta de: \n - Motor: {self.vehiculo.motor}. \n - Ruedas: {self.vehiculo.ruedas}. \n - Puertas: {self.vehiculo.puertas}. \n - Tiene Aireacondicionado: {'Sí' if self.vehiculo.aire_acondicionado else 'No'}"
