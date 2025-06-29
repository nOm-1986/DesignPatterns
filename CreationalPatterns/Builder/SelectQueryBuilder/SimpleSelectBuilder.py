from SqlQueryBuilder import SqlQueryBuilder

class SimpleSelectBuilder(SqlQueryBuilder):
  
  def select(self, columnas):
    self._consulta.columnas = columnas
    return self
  
  def from_tabla(self, tabla):
    self._consulta.tabla = tabla
    return self

  def condicion(self, condicion):
    self._consulta.condiciones.append(condicion)
    return self

  def limite(self, limite):
    if limite <= 0:
      raise ValueError("LIMIT debe ser un número positivo.")
    self._consulta.limite = limite
    return self