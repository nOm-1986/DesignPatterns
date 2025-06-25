from VehicleFactory import VehicleFactory
from Bike import Bike

class BikeFactory(VehicleFactory):

  def create_vehicle(self):
    return Bike()