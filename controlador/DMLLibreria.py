from controlador.Conexion import Conexion
from controlador.DML import DML
from modelo.Libreria import Libreria

class DMLLibreria:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def altas(self, libreria: Libreria):
        self.dml.altas_bajas_cambios(f"""INSERT INTO libreria.libreria(libreria_id, nombre_libreria, telefono, rfc, cp, direccion) 
                                        VALUES(nextval('libreria.nextlib'), '{libreria.nombre}', {libreria.telefono_libreria}, '{libreria.RFC}', {libreria.CP}, '{libreria.direccion}')""")

    def bajas(self, id: int):
        self.dml.altas_bajas_cambios(f"DELETE FROM libreria.libreria WHERE libreria_id={id}")
    
    def cambios(self, libreria: Libreria):
        self.dml.altas_bajas_cambios(f"""UPDATE libreria.libreria 
                                        SET direccion='{libreria.direccion}', 
                                        RFC='{libreria.RFC}', 
                                        telefono={libreria.telefono_libreria},
                                        nombre_libreria='{libreria.nombre}',
                                        cp={libreria.CP}
                                        WHERE libreria_id={libreria.libreriaId}""")

    def consultas(self, id:int):
        return self.dml.consulta(f"""
                                SELECT l.libreria_id, l.nombre_libreria, l.telefono, p.nombre_pais, c.nombre_ciudad,
                                m.nombre_municipio, l.direccion, CONCAT(e.nombre_persona, ' ', e.apellido_paterno, ' ', e.apellido_materno)
                                FROM libreria.libreria as l, libreria.encargado as e, libreria.municipio as m,
                                    libreria.ciudad as c, libreria.pais as p
                                WHERE libreria_id = {id}
                                AND e.rfc = l.rfc
                                AND m.cp = l.cp
                                AND c.ciudad_id = m.ciudad_id
                                AND p.pais_id = c.pais_id
                                ORDER BY libreria_id""")