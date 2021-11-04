from datetime import datetime
class Historial_precios:
    ISBN:str
    precio_antiguo:float
    precio_nuevo:float
    fecha_modificacion:datetime
    
    def __init__(self,ISBN:str,precio_atiguo:float,precio_nuevo:float,fecha_modificacion:datetime) -> None:
        self.ISBN = ISBN
        self.precio_antiguo = precio_atiguo
        self.precio_nuevo = precio_nuevo
        self.fecha_modificacion = fecha_modificacion