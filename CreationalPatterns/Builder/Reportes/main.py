from Director import Director
from ReporteMesBuilderl import ReporteMesBuilder
from ReporteAnualBuilder import ReporteAnualBuilder



if __name__ == "__main__":
    datos_mensuales = [
        {"categoría": "Ventas", "ingresos": 12000, "egresos": 4000},
        {"categoría": "Servicios", "ingresos": 8000, "egresos": 2500},
        {"categoría": "Consultoría", "ingresos": 5000, "egresos": 1000},
    ]
    datos_anuales = [
        {"mes": "Enero", "ingresos": 10000, "egresos": 3000},
        {"mes": "Febrero", "ingresos": 9500, "egresos": 2800},
        {"mes": "Marzo", "ingresos": 12000, "egresos": 3500},
        {"mes": "Abril", "ingresos": 11000, "egresos": 3200},
        {"mes": "Mayo", "ingresos": 10500, "egresos": 3100},
        {"mes": "Junio", "ingresos": 9800, "egresos": 2900},
        {"mes": "Julio", "ingresos": 11500, "egresos": 3300},
        {"mes": "Agosto", "ingresos": 12500, "egresos": 3700},
        {"mes": "Septiembre", "ingresos": 11900, "egresos": 3400},
        {"mes": "Octubre", "ingresos": 13000, "egresos": 3900},
        {"mes": "Noviembre", "ingresos": 12700, "egresos": 3600},
        {"mes": "Diciembre", "ingresos": 14000, "egresos": 4200},
    ]
    # Generar reporte mensual
    builder_mensual = ReporteMesBuilder()
    director = Director(builder_mensual)
    reporte_mensual = director.construir_reporte_mensual("Abril", 2025, datos_mensuales)
    reporte_mensual.mostrar()

    print("\n" + "="*50 + "\n")

    # Generar reporte anual
    builder_anual = ReporteAnualBuilder()
    director = Director(builder_anual)
    reporte_anual = director.construir_reporte_anual(2024, datos_anuales)
    reporte_anual.mostrar()