from controlador.Conexion import Conexion
from controlador.DML import DML
from modelo.Pais import Pais

class DMLPais:
    dml: DML

    def __init__(self, conexion: Conexion):
        self.dml = DML(conexion)

    def altas(self, pais: Pais):
        self.dml.altas_bajas_cambios(f"INSERT INTO Libreria.pais VALUES({pais.paisId}, '{pais.nombre_pais}')")

    def bajas(self, id: int):
        self.dml.altas_bajas_cambios(f"DELETE FROM Libreria.pais WHERE paisid={id}")
    
    def cambios(self, pais: Pais):
        self.dml.altas_bajas_cambios(f"UPDATE Libreria.pais SET nombre_pais={pais.nombre_pais} WHERE pais_id={pais.paisId}")

    def consultas(self, txt: str):
        self.dml.consulta(f"SELECT * FROM Libreria.pais WHERE nombre_pais like '{txt}'")

'''
    CREATE SEQUENCE nombre START WITH 1 INCREMENT BY 1 NO LIMIT 
    INSERT INTO tabla VALUES (nombre.nextval, otro)
'''