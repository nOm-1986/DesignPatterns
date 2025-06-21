from ComputadoraGamerBuilder import ComputadoraGamerBuilder
from ComputadoraOficinaBuilder import ComputadoraOficinaBuilder
from Director import Director
if __name__ == "__main__":
    print("--- Computadora para Gaming ---")
    builder_gamer = ComputadoraGamerBuilder()
    director = Director()
    pc_gamer = director.construir_computadora_completa(builder_gamer)
    print(pc_gamer)

    print("--- Computadora para Oficina ---")
    builder_oficina = ComputadoraOficinaBuilder()
    director = Director()
    pc_oficina = director.construir_computadora_completa(builder_oficina)
    print(pc_oficina)