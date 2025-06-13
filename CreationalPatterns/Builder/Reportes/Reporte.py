class Reporte:

    def __init__(self):
        self.secciones = []

    def agregar_seccion(self, text):
        self.secciones.append(text)
    
    def mostrar(self):
        print("\n".join(self.secciones))