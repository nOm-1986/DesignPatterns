from abc import ABC, abstractmethod

class DocumentoFactory(ABC):
  @abstractmethod
  def crear_documento(self): pass

  def generar_documento(self):
    documento = self.crear_documento()
    documento.set_tipo_documento()
    documento.generar_contenido()
    return documento