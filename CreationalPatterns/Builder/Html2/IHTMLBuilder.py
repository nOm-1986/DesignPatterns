from abc import ABC, abstractmethod
from DocumentoHTML import DocumentoHTML

class IHTMLBuilder(ABC):
    
    def __init__(self):
        self.documento = DocumentoHTML()
    
    @abstractmethod
    def agregar_titulo(self, texto): pass

    @abstractmethod
    def agregar_parrafo(self, texto): pass

    @abstractmethod
    def agregar_enlace(self, texto, url): pass

    def obtener_documento(self):
        return self.documento