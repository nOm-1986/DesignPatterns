from abc import ABC, abstractmethod

class VehicleFactory(ABC):

  @abstractmethod
  def create_vehicle(self): pass

  def order_vehicle(self):
    vehicle = self.create_vehicle()
    vehicle.start()
    vehicle.drive()
    vehicle.stop()
    return vehicle