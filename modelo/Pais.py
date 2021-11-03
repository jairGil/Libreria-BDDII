from modelo.Direccion import Direccion

class Pais(Direccion):
    nombre_pais : str
    
    def __init__(self, nombre_pais: str ) -> None:
        self.nombre_pais = nombre_pais
        
