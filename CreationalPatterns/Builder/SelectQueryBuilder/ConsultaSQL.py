import typing as t

class ConsultaSQL:
  def __init__(self):
    self.columnas: t.List[str] = []
    self.tabla: str = ''
    self.condiciones: t.List[str] = []
    self.limite: int = None
  
  def __str__(self) -> str:
    
    if not self.tabla:
      raise ValueError('La tabla es obligatoria')
    # Construcción de la consulta
    columnas_str = ", ".join(self.columnas) if self.columnas else "*"
    query_str = f"SELECT {columnas_str} FROM {self.tabla}"

    if self.condiciones:
      condiciones_str = " AND ".join(self.condiciones)
      query_str += f" WHERE {condiciones_str}"
    
    if self.limite is not None:
      query_str += f" LIMIT {self.limite}"
    
    return query_str + ";"