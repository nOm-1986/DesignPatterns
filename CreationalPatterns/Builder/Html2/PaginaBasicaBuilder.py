from IHTMLBuilder import IHTMLBuilder

class PaginaBasicaBuilder(IHTMLBuilder):

    def agregar_titulo(self, texto):
        self.documento.agregar_parte(f"<head><title>{texto}</title></head>\n<body>\n<h1>{texto}</h1>")
    
    def agregar_parrafo(self, texto):
        self.documento.agregar_parte(f"<p>{texto}</p>")

    def agregar_enlace(self, texto, url):
        self.documento.agregar_parte(f'<a href="{url}">{texto}</a>')