from Computadora import Computadora
from abc import ABC, abstractmethod

class ComputadoraBuilder(ABC):
  
  def __init__(self):
    self.computadora = Computadora()
  
  @abstractmethod
  def set_cpu(self, cpu): pass

  @abstractmethod
  def set_gpu(self, gpu): pass

  @abstractmethod
  def set_ram(self, ram): pass

  @abstractmethod
  def set_disco_duro(self, dd): pass

  @abstractmethod
  def set_fuente_poder(self, fuente):pass

  @abstractmethod
  def set_sistema_operativo(self, so): pass

  def get_result(self):
    return self.computadora