class DocumentoHTML:

    def __init__(self):
        self.partes = []
    
    def agregar_parte(self, html):
        self.partes.append(html)
    
    def render(self):
        return "<!DOCTYPE html>\n<html>\n" + "\n".join(self.partes) + "</html>"