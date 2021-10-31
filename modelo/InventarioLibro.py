from Libreria import Libreria
from Libro import Libro
class InventarioLibro:
    libreriaId:Libreria
    libroISBN:libreriaId
    cantidad:int
    def __init__(self,libreiaId:Libreria,libroISBN:Libro,cantidad) -> None:
        self.libreriaId = libreiaId
        self.libroISBN = libroISBN
        self.cantidad = cantidad