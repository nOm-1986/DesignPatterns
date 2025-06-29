from SimpleSelectBuilder import SimpleSelectBuilder

if __name__ == '__main__':
  consulta_builder = SimpleSelectBuilder()
  consulta_obj = consulta_builder.select(["nombre", "email"]) \
                          .from_tabla("clientes") \
                          .condicion("pais = 'Colombia'") \
                          .condicion("activo = 1") \
                          .condicion("apellido LIKE % a % ") \
                          .limite(10) \
                          .build()
  print(consulta_obj)