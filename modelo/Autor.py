from modelo.Persona import Persona
from modelo.Direccion import Direccion


class Autor(Persona):
    
    def __init__(self, per: Persona) -> None:
        super().__init__(per.rfc, per.nombre, per.apellido_paterno, per.apellido_materno, per.direccion)
