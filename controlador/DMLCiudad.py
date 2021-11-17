from controlador.Conexion import Conexion
from controlador.DML import DML

class DMLCiudad:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def consultas(self, id: int):
        return self.dml.consulta(f"""SELECT ciudad_id, nombre_ciudad, pais_id 
                                        FROM libreria.ciudad
                                        WHERE pais_id = {id}""")