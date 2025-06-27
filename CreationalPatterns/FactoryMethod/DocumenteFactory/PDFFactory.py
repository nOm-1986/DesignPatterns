from DocumentoFactory import DocumentoFactory
from PDFFake import PDFFake

class PDFFactory(DocumentoFactory):
  def crear_documento(self):
    return PDFFake()