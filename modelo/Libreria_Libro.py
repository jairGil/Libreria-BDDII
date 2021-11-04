class InventarioLibro:
    libreria_Id:int
    libro_ISBN:str
    stock:int
    def __init__(self,libreia_Id:int,libro_ISBN:str,stock:int) -> None:
        self.libreriaId = libreia_Id
        self.libroISBN = libro_ISBN
        self.cantidad = stock

