class Libreria:
    libreriaId:int
    telefono_libreria:str
    RFC:str
    CP: int
    direccion:str
    
    def __init__(self,libreriaId:int,telefono_libreria:str,RFC:str,cp:int,direccion:str) -> None:
        self.libreriaId = libreriaId
        self.telefono_libreria = telefono_libreria
        self.RFC = RFC
        self.CP = cp
        self.direccion =direccion
        

