class Computadora:
  def __init__(self):
    self.cpu = None
    self.gpu = None
    self.ram = None
    self.disco_duro = None
    self.fuente_poder = None
    self.sistema_operativo = None
  
  def __str__(self):
    return f"""
      CPU: {self.cpu}
      GPU: {self.gpu}
      RAM: {self.ram}
      Almacenamiento: {self.disco_duro}
      Fuente de poder: {self.fuente_poder}
      Sistema Operativo: {self.sistema_operativo}
    """