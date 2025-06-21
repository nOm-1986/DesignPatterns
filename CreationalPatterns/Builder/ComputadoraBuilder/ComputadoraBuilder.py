from Computadora import Computadora
from abc import ABC, abstractmethod

class ComputadoraBuilder(ABC):
  
  def __init__(self):
    self.computadora = Computadora()
  
  @abstractmethod
  def set_cpu(self): pass

  @abstractmethod
  def set_gpu(self): pass

  @abstractmethod
  def set_ram(self): pass

  @abstractmethod
  def set_disco_duro(self): pass

  @abstractmethod
  def set_fuente_poder(self):pass

  @abstractmethod
  def set_sistema_operativo(self): pass

  def get_result(self):
    return self.computadora