class Libro:
    ISBN:str
    personaID:int
    editorialNombre:str
    año:int
    titulo:str
    precio:int
    categoriaID:int
    def __init__(self,ISBN,personaID,editorialNombre,año,titulo,precio,categoriaID) -> None:
        self.ISBN = ISBN
        self.personaID = personaID
        self.editorialNombre = editorialNombre
        self.año = año
        self.titulo = titulo
        self.precio = precio
        self.categoriaID = categoriaID
