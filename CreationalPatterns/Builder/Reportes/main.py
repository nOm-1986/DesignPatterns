from Director import Director
from ReporteMesBuilderl import ReporteMesBuilder

if __name__ == "__main__":
    datos_mensuales = [
        {"categoría": "Ventas", "ingresos": 12000, "egresos": 4000},
        {"categoría": "Servicios", "ingresos": 8000, "egresos": 2500},
        {"categoría": "Consultoría", "ingresos": 5000, "egresos": 1000},
    ]
    # Generar reporte mensual
    builder_mensual = ReporteMesBuilder()
    director = Director(builder_mensual)
    reporte_mensual = director.construir_reporte_mensual("Abril", 2025, datos_mensuales)
    reporte_mensual.mostrar()