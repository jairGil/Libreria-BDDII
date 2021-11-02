class  Factura:
    factura_ID : int
    rfc : chr
    fecha_Compra : int

def __init__(self, factura_ID : int, rfc : chr, fecha_Compra : int ) -> None:
    self.factura_ID = factura_ID
    self.rfc = rfc
    self.fecha_Compra = fecha_Compra
