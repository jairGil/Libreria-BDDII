from controlador.Conexion import Conexion
from controlador.DML import DML


class DMLFacturas():
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def get_detalles_cliente(self, id_factura: int):
        sql =  f''' SELECT f.factura_id, concat(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                        to_char(f.fecha_compra, 'YYYY-MM-DD')
                        FROM libreria.factura as f, libreria.cliente as c 
                        WHERE f.rfc = c.rfc
                        AND f.factura_id = {id_factura}
                    '''
        return self.dml.consulta(sql)

    def get_detalles_compra(self, id_factura: int):
        sql =  f''' SELECT l.titulo, l.precio, fl.cantidad_libro, fl.cantidad_libro * l.precio
                        FROM libreria.libro as l, libreria.factura_libro as fl 
                        WHERE l.isbn = fl.isbn
                        AND fl.factura_id = {id_factura}
                    '''
        return self.dml.consulta(sql)
