from VehiculoDirector import VehiculoDirector
from MotoBuilder import MotoBuilder
from CamionBuilder import CamionBuilder

if __name__ == "__main__":
    creador = VehiculoDirector()
    moto_builder = MotoBuilder()
    camion_builder = CamionBuilder()
    print("Haciendo una moto")
    moto1 = creador.make_vehiculo(moto_builder)
    print(moto1)
    print("="*20)
    print("Haciendo un camion: ")
    camion1 = creador.make_vehiculo(camion_builder)
    print(camion1)

    