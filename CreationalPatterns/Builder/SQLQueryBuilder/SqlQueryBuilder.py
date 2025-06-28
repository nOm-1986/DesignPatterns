from Sql import Sql
from abc import ABC, abstractmethod
from typing import List

class SqlQueryBuilder(ABC):
  def __init__(self):
    self.sql = Sql()

  @abstractmethod
  def select(self, columns: List[str]): pass

  @abstractmethod
  def from_tabla(self, tabla): pass

  @abstractmethod
  def condicion(self, columna, condicion, valor): pass

  @abstractmethod
  def limite(self, limite): pass

  @abstractmethod
  def build(self): pass


{
  [],
  [],
  [],
}
