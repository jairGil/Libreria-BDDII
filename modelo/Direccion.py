from modelo.Municipio import Municipio

class Direccion:
    direccionId: int
    calle: str
    numero_interior : str
	numero_exterior: str
    municipio: Municipio
    
    def __init__(self, direccionId: int, calle: str, numero_interior: str, numero_exterior: str, municipio:Municipio) -> None:
        self.direccionId = direccionId
        self.calle = calle
        self.numero_interior = numero_interior
        self.numero_exterior = numero_exterior
        self.municipio = municipio 
        