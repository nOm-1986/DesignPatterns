from tabulate import tabulate
from Reporte import Reporte
from ReporteBuilder import ReporteBuilder

class ReporteAnualBuilder(ReporteBuilder):

    def __init__(self):
        self.reporte = Reporte()
    
    def agregar_encabezado(self, anio):
        self.reporte.agregar_seccion(f"=== Reporte Anual: {anio} ===\n")

    def agregar_tabla_datos(self, datos_anuales):
        tabla = [[d["mes"], d["ingresos"], d["egresos"]] for d in datos_anuales]
        headers = ["Mes", "Ingresos", "Egresos"]
        self.reporte.agregar_seccion(tabulate(tabla, headers=headers, tablefmt="github") + "\n")
    
    def agregar_resumen(self,datos_anuales):
        total_ingresos = sum(d["ingresos"] for d in datos_anuales)
        total_egresos = sum(d["egresos"] for d in datos_anuales)
        self.reporte.agregar_seccion(f"Total Ingresos: ${total_ingresos}")
        self.reporte.agregar_seccion(f"Total Egresos:  ${total_egresos}")
        self.reporte.agregar_seccion(f"Balance Neto:   ${total_ingresos - total_egresos}\n")

    def agregar_grafica(self):
        self.reporte.agregar_seccion("[Gráfica de barras simulada]\n")

    def agregar_pie_pagina(self):
        self.reporte.agregar_seccion("------------------------------------")
        self.reporte.agregar_seccion("Reporte anual generado automáticamente.")

    def obtener_reporte(self):
        return self.reporte