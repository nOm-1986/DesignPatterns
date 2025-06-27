from abc import ABC, abstractmethod

class IDocument(ABC):
  
  @abstractmethod
  def set_tipo_documento(self): pass

  @abstractmethod
  def generar_contenido(self): pass