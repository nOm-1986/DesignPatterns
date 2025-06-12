from Html import Html
from IHtml import IHtml

class HomeBuilder(IHtml):

    def __init__(self):
        self.html = Html()

    def add_titulo(self):
        self.html.titulo = "<h1>Home principal</h1>"

    def add_encabezado(self):
        self.html.encabezado = "<h2>Encabezados home</h2>"

    def add_parrafo(self):
        self.html.parrafos = "<p>Lorem ipsum para el home</p>"

    def add_enlaces(self):
        self.html.enlaces = "<a href='#'>Enlace a pepito</a>"

    def get_html(self):
        return f"Home Page: \n {self.html.titulo}. \n {self.html.encabezado} \n {self.html.parrafos} \n {self.html.enlaces}"