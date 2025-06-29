from ConsultaSQL import ConsultaSQL
from abc import ABC, abstractmethod
import typing as t

class SqlQueryBuilder(ABC):
  def __init__(self):
    self.reset()
  
  def reset(self):
    self._consulta = ConsultaSQL()

  @abstractmethod
  def select(self, columns: t.List[str]): pass

  @abstractmethod
  def from_tabla(self, tabla: str): pass

  @abstractmethod
  def condicion(self, condicion: str): pass

  @abstractmethod
  def limite(self, limite: int): pass

  def build(self):
    consulta_finalizada = self._consulta
    self.reset()
    return consulta_finalizada

  
