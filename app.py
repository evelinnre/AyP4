class Estudiante:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

estudiante1 = Estudiante("Juan", 1111)
print(estudiante1.nombre)