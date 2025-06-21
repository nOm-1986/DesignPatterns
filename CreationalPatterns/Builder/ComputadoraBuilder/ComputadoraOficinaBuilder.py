from ComputadoraBuilder import ComputadoraBuilder

class ComputadoraOficinaBuilder(ComputadoraBuilder):
  def set_cpu(self):
    self.computadora.cpu = "Intel Core i5"

  def set_gpu(self):
      self.computadora.gpu = "Gráficos integrados"

  def set_ram(self):
      self.computadora.ram = "8GB"

  def set_disco_duro(self):
      self.computadora.almacenamiento = "512GB SSD"

  def set_fuente_poder(self):
      self.computadora.fuente_poder = "450W"

  def set_sistema_operativo(self):
      self.computadora.sistema_operativo = "Windows 10"