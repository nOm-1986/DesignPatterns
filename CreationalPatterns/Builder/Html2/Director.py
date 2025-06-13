from IHTMLBuilder import IHTMLBuilder

class Director:
    def __init__(self, builder: IHTMLBuilder):
        self.builder = builder
    
    def construir_pagina_ejemplo(self):
        self.builder.agregar_titulo("Mi página")
        self.builder.agregar_parrafo("Esta es una página web generada con el patron builder")
        self.builder.agregar_parrafo("Págian creada paso a paso")
        self.builder.agregar_enlace("Visita FS", "https://formasegura.com")
        self.builder.documento.agregar_parte("\n</body>")