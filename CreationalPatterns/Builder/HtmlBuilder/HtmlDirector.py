from Html import Html
from IHtml import IHtml

class HtmlDirector:

    def make_html(self, html_builder: IHtml)-> str:
        html_builder.add_titulo()
        html_builder.add_encabezado()
        html_builder.add_parrafo()
        html_builder.add_enlaces()
        return html_builder.get_html()
    