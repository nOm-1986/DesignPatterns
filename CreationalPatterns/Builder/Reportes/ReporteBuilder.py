from abc import ABC, abstractmethod
from Reporte import Reporte

class ReporteBuilder(ABC):

    def __init__(self):
        self.reporte = Reporte()

    @abstractmethod
    def agregar_encabezado(self, mes, anio): pass

    @abstractmethod
    def agregar_tabla_datos(self, datos): pass

    @abstractmethod
    def agregar_grafica(self):pass

    @abstractmethod
    def agregar_pie_pagina(self): pass

    def obtener_reporte(self):
        return self.reporte