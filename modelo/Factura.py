from datetime import datetime
class  Factura:
    factura_ID : int
    rfc : str
    fecha_Compra : datetime

def __init__(self, factura_ID : int, rfc : str, fecha_Compra : datetime ) -> None:
    self.factura_ID = factura_ID
    self.rfc = rfc
    self.fecha_Compra = fecha_Compra
