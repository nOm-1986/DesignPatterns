from abc import ABC, abstractmethod

class IVehicle:
  @abstractmethod
  def start(self):pass

  @abstractmethod
  def stop(self):pass

  @abstractmethod
  def drive(self): pass