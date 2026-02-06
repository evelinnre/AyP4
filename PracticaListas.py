class Nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, documento, nombre):
        nuevo = Nodo(documento, nombre)

        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        # Recorrer hasta el último nodo
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        # Enlazar el último con el nuevo
        actual.siguiente = nuevo

lista = Lista()
lista.insertar_al_final(123, "Ana")
lista.insertar_al_final(456, "Luis")
lista.insertar_al_final(789, "María")

    
               