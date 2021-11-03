class Libreria:
    libreriaId:int
    direccionId:int
    RFC:str
    telefono_libreria:str
    

    def __init__(self,libreriaId:int,direccionId:int,RFC:str,telefono:str) -> None:
        self.libreriaId = libreriaId
        self.direccionId = direccionId
        self.RFC = RFC
        self.telefono_libreria = telefono
        

