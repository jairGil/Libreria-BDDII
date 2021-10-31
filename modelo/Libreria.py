class Libreria:
    libreriaId:int
    direccionId:int
    telefono:str
    personaId:int

    def __init__(self,libreriaId,direccionId,telefono,personaId) -> None:
        self.libreriaId = libreriaId
        self.direccionId = direccionId
        self.telefono = telefono
        self.personaId = personaId
