from controlador.Conexion import Conexion
from controlador.DML import DML


class DMLReportes():
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)
        self.columnas = ["ID factura", "Nombre del cliente", "Fecha de compra"]

    def reporte_dia(self, fecha: str):
        sql =  f""" SELECT f.factura_id,  
                    CONCAT(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                    TO_CHAR(f.fecha_compra, 'DD/Month/YYYY')
                    FROM libreria.factura as f, libreria.cliente as c
                    WHERE fecha_compra = TO_DATE('{fecha}', 'dd/Month/YYYY') 
                    AND f.rfc = c.rfc
                    ORDER BY f.factura_id
                """
        return self.columnas, self.dml.consulta(sql)

    def reporte_mes(self, fecha: str):
        f = fecha.split("/")
        sql =  f""" SELECT f.factura_id,  
                    CONCAT(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                    TO_CHAR(f.fecha_compra, 'DD/Month/YYYY')
                    FROM libreria.factura as f, libreria.cliente as c
                    WHERE EXTRACT(MONTH FROM DATE(f.fecha_compra)) = EXTRACT(MONTH FROM TO_DATE('{f[0]}', 'Month')) 
                    AND EXTRACT(YEAR FROM DATE(f.fecha_compra)) = EXTRACT(YEAR FROM TO_DATE('{f[1]}', 'YYYY'))
                    AND f.rfc = c.rfc
                    ORDER BY f.fecha_compra, f.factura_id
                """
        return self.columnas, self.dml.consulta(sql)

    def reporte_anio(self, fecha: str):
        sql =  f""" SELECT f.factura_id, 
                    CONCAT(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                    TO_CHAR(f.fecha_compra, 'DD/Month/YYYY')
                    FROM libreria.factura as f, libreria.cliente as c
                    WHERE EXTRACT(YEAR FROM DATE(f.fecha_compra)) = EXTRACT(YEAR FROM TO_DATE('{fecha}', 'YYYY'))
                    AND f.rfc = c.rfc
                    ORDER BY f.fecha_compra, f.factura_id
                """
        return self.columnas, self.dml.consulta(sql)

    def reporte_personalizado(self, fecha_inicio: str, fecha_fin: str):
        sql =  f""" SELECT f.factura_id, 
                    CONCAT(c.nombre_persona, ' ', c.apellido_paterno, ' ', c.apellido_materno), 
                    TO_CHAR(f.fecha_compra, 'DD/Month/YYYY')
                    FROM libreria.factura as f, libreria.cliente as c
                    WHERE f.fecha_compra BETWEEN TO_DATE('{fecha_inicio}', 'dd/Month/YYYY') 
                        AND TO_DATE('{fecha_fin}', 'dd/Month/YYYY') 
                    AND f.rfc = c.rfc
                    ORDER BY f.fecha_compra, f.factura_id
                """
        return self.columnas, self.dml.consulta(sql)
