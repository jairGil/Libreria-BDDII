from controlador.Conexion import Conexion
from controlador.DML import DML
from modelo.Municipio import Municipio

class DMLPais:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def altas(self, municipio: Municipio):
        self.dml.altas_bajas_cambios(f"INSERT INTO Libreria.municipio VALUES('{municipio.codigo_postal}', '{municipio.nombre_municipio}', '{municipio.ciudad}')")

    def bajas(self, id: int):
        self.dml.altas_bajas_cambios(f"DELETE FROM Libreria.municipio WHERE libreria_id={id}")
    
    def cambios(self, municipio: Municipio):
        self.dml.altas_bajas_cambios(f"UPDATE Libreria.municipio SET nombre_municipio={municipio.nombre_municipio}, ciudad_id={municipio.ciudad} WHERE codigo_postal={municipio.codigo_postal}")

    def consultas(self, txt: str):
        self.dml.consulta(f"SELECT * FROM Libreria.municipio WHERE codigo_postal like '{txt}'")