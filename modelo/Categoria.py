class Categoria:
    categoria_ID:int
    descripcion:str
    def __init__(self,categoria_ID:int,descripcion:str) -> None:
        self.idCategoria = categoria_ID
        self.descripcion = descripcion 