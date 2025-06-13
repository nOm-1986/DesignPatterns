from ReporteBuilder import ReporteBuilder

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_reporte_mensual(self, mes, anio, datos_mensuales):
        self.builder.agregar_encabezado(mes, anio)
        self.builder.agregar_tabla_datos(datos_mensuales)
        self.builder.agregar_grafica()
        self.builder.agregar_pie_pagina()
        return self.builder.obtener_reporte()

    def construir_reporte_anual(self, anio, datos):
        self.builder.agregar_encabezado(anio)
        self.builder.agregar_tabla_datos(datos)
        self.builder.agregar_resumen(datos)
        self.builder.agregar_pie_pagina()
        return self.builder.obtener_reporte()