from abc import ABC, abstractmethod

class IHtml(ABC):

    @abstractmethod
    def add_titulo(self):
        pass

    @abstractmethod
    def add_encabezado(self):
        pass

    @abstractmethod
    def add_parrafo(self):
        pass

    @abstractmethod
    def add_enlaces(self):
        pass

    @abstractmethod
    def get_html(self):
        pass