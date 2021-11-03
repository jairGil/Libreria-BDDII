from modelo.Pais import Pais

class Ciudad:
    ciudadId : int
    nombre_ciudad : str
    pais: Pais

    def __init__(self, ciudadId : int, nombre_ciudad: str, pais: Pais ) -> None:
        self.ciudadId = ciudadId
        self.nombre_ciudad = nombre_ciudad
        self.pais = pais