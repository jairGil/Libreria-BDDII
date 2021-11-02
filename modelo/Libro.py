from Autor import Autor
from Categoria import Categoria
class Libro:
    ISBN:str
    personaID:int
    editorialNombre:str
    año:int
    titulo:str
    precio:int
    categoriaID:categoriaID
    def __init__(self,ISBN:set,personaID:Autor,editorialNombre,año,titulo,precio,categoriaID:Categoria) -> None:
        self.ISBN = ISBN
        self.personaID = personaID
        self.editorialNombre = editorialNombre
        self.año = año
        self.titulo = titulo
        self.precio = precio
        self.categoriaID = categoriaID
