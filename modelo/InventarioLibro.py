class InventarioLibro:
    libreriaId:int
    libroISBN:str
    cantidad:int
    def __init__(self,libreiaId:int,libroISBN:str,cantidad:int) -> None:
        self.libreriaId = libreiaId
        self.libroISBN = libroISBN
        self.cantidad = cantidad

