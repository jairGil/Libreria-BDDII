class Libreria:
    libreriaId:int
    direccionId:int
    telefono:str
    personaId:int

    def __init__(self,libreriaId:int,direccionId:int,telefono:str,personaId:int) -> None:
        self.libreriaId = libreriaId
        self.direccionId = direccionId
        self.telefono = telefono
        self.personaId = personaId

lib = Libreria(1,2000,"7455464564",5)
print(lib.libreriaId)