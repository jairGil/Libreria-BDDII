class Libreria:
    libreriaId:int
    telefono_libreria:str
    RFC:str
    CP: int
    direccion:str
    
    def __init__(self,nombre:str,telefono_libreria:str,RFC:str,cp:int,direccion:str) -> None:
        self.nombre = nombre
        self.telefono_libreria = telefono_libreria
        self.RFC = RFC
        self.CP = cp
        self.direccion =direccion
        

