from IVehiculoBuilder import IVehiculosBuilder

class VehiculoDirector:
    
    def make_vehiculo(self, vehiculo_builder: IVehiculosBuilder):
        vehiculo_builder.set_motor()
        vehiculo_builder.set_puertas()
        vehiculo_builder.set_ruedas()
        vehiculo_builder.set_aire_acondicionado()
        return vehiculo_builder.get_vehiculo()
        #return vehiculo_builder.vehiculo