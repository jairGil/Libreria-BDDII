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
        self.dml.altas_bajas_cambios(f"DELETE FROM Libreria.libreria WHERE libreria_id={id}")
    
    def cambios(self, libreria: Libreria):
        self.dml.altas_bajas_cambios(f"UPDATE Libreria.libreria SET direccion_id={libreria.direccionId}, RFC={libreria.RFC}, telefono_libreria={libreria.telefono_libreria} WHERE pais_id={libreria.libreriaId}")

    def consultas(self, txt: str):
        self.dml.consulta(f"SELECT * FROM Libreria.libreria WHERE RFC like '{txt}'")