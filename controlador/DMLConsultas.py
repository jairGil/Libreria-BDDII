from controlador.DML import DML
from controlador.Conexion import Conexion


class DMLConsultas:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def get_librerias(self):
        encabezados = ["ID", "Nombre de Libreria", "Telefono", "Encargado", "CP", "Direccion"]
        sql =   """ SELECT l.libreria_id, l.nombre_libreria, l.telefono, 
                    concat(e.nombre_persona, ' ', e.apellido_paterno, ' ', e.apellido_materno), l.cp, l.direccion 
                    FROM libreria.libreria as l, libreria.encargado as e
                    WHERE l.rfc = e.rfc
                """
        datos = self.dml.consulta(sql)
        return encabezados, datos

    def get_libros(self):
        encabezados = ["ISBN", "Titulo", "Precio", "Categoria"]
        sql =   """ SELECT l.isbn, l.titulo, l.precio, c.nombre_categoria 
                    FROM libreria.libro as l, libreria.categoria as c 
                    WHERE l.categoria_id = c.categoria_id
                """
        datos = self.dml.consulta(sql)
        return encabezados, datos
    
    def get_encargados(self):
        encabezados = ["RFC", "Nombre" , "CP", "Direccion"]
        sql =   """ SELECT rfc, concat(nombre_persona, ' ', apellido_paterno, ' ', apellido_materno), cp, direccion 
                    FROM libreria.encargado
                """
        datos = self.dml.consulta(sql)
        return encabezados, datos
