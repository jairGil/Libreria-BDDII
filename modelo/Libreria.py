from Persona import Persona
from Direccion import Direccion
class Libreria:
    libreriaId:int
    direccionId:Direccion
    telefono:str
    personaId:Persona

    def __init__(self,libreriaId,direccionId:Direccion,telefono,personaId:Persona) -> None:
        self.libreriaId = libreriaId
        self.direccionId = direccionId
        self.telefono = telefono
        self.personaId = personaId
