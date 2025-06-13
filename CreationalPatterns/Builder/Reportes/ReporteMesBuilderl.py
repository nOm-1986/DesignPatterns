from ReporteBuilder import ReporteBuilder
from tabulate import tabulate

class ReporteMesBuilder(ReporteBuilder):

    def agregar_encabezado(self, mes, anio):
        self.reporte.agregar_seccion(f"=== Reporte mensual {mes} {anio} ===\n")
    
    def agregar_tabla_datos(self, datos_mensuales):
        tabla = [[d["categoría"], d["ingresos"], d["egresos"]] for d in datos_mensuales]
        encabezados = ["Categoría", "Ingresos", "Egresos"]
        self.reporte.agregar_seccion(tabulate(tabla, headers=encabezados, tablefmt="github") + "\n")

    def agregar_grafica(self):
        self.reporte.agregar_seccion("[Gráfica de barras simulada]\n")
    
    def agregar_pie_pagina(self):
        self.reporte.agregar_seccion("------------------------------------")
        self.reporte.agregar_seccion("Generado automáticamente por el sistema de reportes financieros.")