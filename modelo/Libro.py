class Libro:
    ISBN:str
    personaID:int
    editorialNombre:str
    año:int
    titulo:str
    precio:float
    categoriaID:int
    def __init__(self,ISBN:str,personaID:int,editorialNombre:str,año:int,titulo:str,precio:int,categoriaID:int) -> None:
        self.ISBN = ISBN
        self.personaID = personaID
        self.editorialNombre = editorialNombre
        self.año = año
        self.titulo = titulo
        self.precio = precio
        self.categoriaID = categoriaID


