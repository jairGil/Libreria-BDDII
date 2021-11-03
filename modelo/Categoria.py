class Categoria:
    idCategoria:int
    descripcion:str
    def __init__(self,idCategoria:int,descripcion:str) -> None:
        self.idCategoria = idCategoria
        self.descripcion = descripcion 