from ComputadoraBuilder import ComputadoraBuilder

class ComputadoraGamerBuilder(ComputadoraBuilder):
  
  def set_cpu(self, cpu):
    self.computadora.cpu = cpu
  
  def set_gpu(self, gpu):
    self.computadora.gpu = gpu

  def set_ram(self, ram):
    self.computadora.ram = ram

  def set_disco_duro(self, dd):
    self.computadora.disco_duro = dd
  
  def set_fuente_poder(self, fuente):
    self.computadora.fuente_poder = fuente
  
  def set_sistema_operativo(self, so):
    self.computadora.sistema_operativo = so