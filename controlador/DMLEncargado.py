from controlador.Conexion import Conexion
from controlador.DML import DML

class DMLEncargado:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def consultas(self, cp: int):
        return self.dml.consulta(f"""SELECT rfc, CONCAT(nombre_persona, ' ', apellido_paterno, ' ', apellido_materno), cp 
                                        FROM libreria.encargado
                                        WHERE cp = {cp}""")