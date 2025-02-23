#class: Relación directa con un objeto (entidad u objeto)
#def: Acciones o funciones del objeto

class Personas():
    def __init__(self):
        # Atributos del objeto
        self.nombre = "Andres"
        self.edad = 42
        self.estatura = 193
        self.peso = 35.6

persona = Personas()
print("Nombre: ",persona.nombre," Edad: ",persona.edad," Estatura: ",persona.estatura," cms")
