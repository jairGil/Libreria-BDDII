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

    def crearXML(self,id:int):
        f = open('temp.xml', 'w', encoding='UTF8')
        sql = f"""SELECT XMLELEMENT(name factura,XMLCONCAT((SELECT XMLCONCAT(
                                    XMLELEMENT(name factura_id,factura.factura_id),
                                            XMLELEMENT(name nombre_cliente, cliente.nombre_persona),
                                            XMLELEMENT(name apellido_paterno, cliente.apellido_paterno),
                                            XMLELEMENT(name apellido_materno, cliente.apellido_materno),
                                            XMLELEMENT(name direccion, cliente.direccion),
                                            XMLELEMENT(name cp, cliente.cp),
                                            XMLELEMENT(name fecha_compra, factura.fecha_compra))
                                    FROM libreria.factura, libreria.cliente
                                    WHERE factura.factura_id = {id}
                                    AND factura.rfc = cliente.rfc),(SELECT XMLELEMENT(name compra, XMLAGG(detalles))
                                FROM (SELECT XMLELEMENT(name libro,
                                        XMLCONCAT(XMLELEMENT(name ISBN, libro.isbn),
                                            XMLELEMENT(name titulo, libro.titulo),
                                            XMLELEMENT(name precio, libro.precio),
                                            XMLELEMENT(name cantidad, factura_libro.cantidad_libro))
                                        ) as detalles
                                    FROM libreria.factura_libro, libreria.libro
                                    WHERE factura_libro.factura_id = {id}
                                    AND factura_libro.isbn = libro.isbn) t)))"""
        f.write(self.dml.consulta(sql)[0][0])
        f.close()

    