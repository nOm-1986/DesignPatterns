from Director import Director
from PaginaBasicaBuilder import PaginaBasicaBuilder

if __name__ == "__main__":
    builder = PaginaBasicaBuilder()
    director = Director(builder)
    director.construir_pagina_ejemplo()

    pagina = builder.obtener_documento()
    print(pagina.render())