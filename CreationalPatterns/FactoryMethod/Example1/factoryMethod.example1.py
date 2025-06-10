from abc import ABC, abstractmethod

class IVehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def drive(self):
        pass

   
#Clase abstracta para crear los vehiculos
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass
    
    def order_vehicle(self):
        vehicle = self.create_vehicle()
        vehicle.start()
        vehicle.drive()
        vehicle.stop()
        return vehicle
    

#clases concretas
class Bike(IVehicle):
    def start(self):
        print("Pedalea caramba, esto no tiene encendido flojo")

    def stop(self):
        print("Freno de pieee ojo te caes boludo ")

    def drive(self):
        print("Equilibrio, es fácil..... Manejando la bici ")


class Car(IVehicle):
    def start(self):
        print("Encendiendo el automovil")
    
    def stop(self):
        print("Deteniendo el carro ")
    
    def drive(self):
        print("Manejando el carro ")


class Motorcycle(IVehicle):
    def start(self):
        print("Encendiendo la moto")
    
    def stop(self):
        print("Deteniendo la moto")
    
    def drive(self):
        print("Manejando la moto")



class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


vehicle_factory = CarFactory()
vehicle = vehicle_factory.order_vehicle()
print(f"You have used a {vehicle.__class__.__name__}.")