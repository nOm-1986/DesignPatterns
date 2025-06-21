from ComputadoraBuilder import ComputadoraBuilder

class ComputadoraGamerBuilder(ComputadoraBuilder):
  
  def set_cpu(self):
    self.computadora.cpu = "Intel Core i9"
  
  def set_gpu(self):
    self.computadora.gpu = "NVIDIA RTX 4080"

  def set_ram(self):
    self.computadora.ram = "32GB"

  def set_disco_duro(self):
    self.computadora.disco_duro = "2TB SSD"
  
  def set_fuente_poder(self):
    self.computadora.fuente_poder = "850W"
  
  def set_sistema_operativo(self):
    self.computadora.sistema_operativo = "Windows 11"