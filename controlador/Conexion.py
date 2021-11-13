from typing import Tuple
import psycopg2


class Conexion:
    usuario: str
    contrasena: str
    puerto: str
    host: str
    database: str
    conexion: psycopg2

    def __init__(self, database: str, usuario: str, contrasena: str, puerto: str, host: str):
        self.database = database
        self.usuario = usuario
        self.contrasena = contrasena
        self.puerto = puerto
        self.host = host
        self.conexion = None

    def conectar(self):
        try:
            # connect to the PostgreSQL server
            self.conexion = psycopg2.connect(f"dbname={self.database} host={self.host} port={self.puerto} user={self.usuario} password={self.contrasena}")

            msg = "Conexion exitosa"
        except (psycopg2.DatabaseError) as error:
            if self.conexion is None:
                msg = "Conexion no realizada\n"
            msg += error.__str__()

        return self.conexion, msg
    
    def desconectar(self):
        try:
            self.conexion.close()
        except AttributeError:
            pass


if __name__ == '__main__':
    from DML import *
    conexion = Conexion("postgres", "postgres", "1710", "5432", "localhost")
    dml = DML(conexion)
    datos = dml.consulta("select * from hr.employee")
    print(datos)
    conexion.desconectar()