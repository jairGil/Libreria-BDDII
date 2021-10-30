from modelo.Persona import Persona


class Cliente(Persona):
    email: str
    tlefono: str

    def __init__(self, per: Persona, email, telefono) -> None:
        super().__init__(per.rfc, per.nombre, per.apellido_paterno, per.apellido_materno, per.direccion)
        self.email = email
        self.tlefono = telefono
