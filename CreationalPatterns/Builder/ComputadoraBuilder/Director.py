from ComputadoraBuilder import ComputadoraBuilder
class Director:

  def construir_computadora_completa(self, builder: ComputadoraBuilder):
    builder.set_cpu()
    builder.set_gpu()
    builder.set_ram()
    builder.set_disco_duro()
    builder.set_fuente_poder()
    builder.set_sistema_operativo()
    return builder.get_result()