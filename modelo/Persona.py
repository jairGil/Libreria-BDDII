from modelo.Direccion import Direccion


class Persona:
    rfc: str
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    direccion: Direccion

    def __init__(self, rfc: str, nombre: str, apellido_paterno: str, apellido_materno: str, direccion: Direccion) -> None:
        self.rfc = rfc
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.direccion = direccion
