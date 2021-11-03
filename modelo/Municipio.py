from modelo.Ciudad import Ciudad

class Municipio:
    municipioId: int
    codigo_postal: str
    nombre_municipio : str
	ciudad: Ciudad
    

    def __init__(self,municipioId: int, codigo_postal: str, nombre_municipio: str, ciudad: Ciudad ) -> None:
        self.municipioId = municipioId
        self.codigo_postal = codigo_postal
        self.nombre_municipio = nombre_municipio
        self.ciudad = ciudad