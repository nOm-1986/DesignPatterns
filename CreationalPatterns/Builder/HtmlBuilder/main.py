from HomeBuilder import HomeBuilder
from HtmlDirector import HtmlDirector

if __name__ == "__main__":
    creador = HtmlDirector()
    home_builder = HomeBuilder()
    home_page = creador.make_html(home_builder)
    print(home_page)