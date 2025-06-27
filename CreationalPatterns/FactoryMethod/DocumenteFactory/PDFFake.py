from IDocument import IDocument

class PDFFake(IDocument):
  def set_tipo_documento(self):
    print(f'Documento tipo PDF.....')

  def generar_contenido(self):
    print(f'Documento generado en tipo PDF......')