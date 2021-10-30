class Persona:

    def __init__(self, edad: int, nombre: str, apellido) -> None:
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido

    def getNombre(self):
        return self.nombre

class Trabajador(Persona):
    def __init__(self, persona: Persona):
        super().__init__(persona.edad, persona.nombre, persona.apellido)

p = Persona(23, "Josue", "afb")
# print(p.__apellido)
t = Trabajador(p)
print(t.getNombre())