class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class Lista:
    def __init__(self):
        self.cabeza = None
        self.siguiente = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

         
    def contar(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo.siguiente is None:
            return 0
        return self.contar(nodo.siguiente) + 1
    
    def sumar(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo.siguiente is None:
            return 0
        return self.sumar(nodo.siguiente) + nodo.dato
    
    def buscar(self, dato, nodo=None, primera_llamada=True):
        if primera_llamada:
            nodo = self.cabeza
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        return self.buscar(dato, nodo.siguiente, False)
    
    def mostrar(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return
        print(nodo.dato)
        self.mostrar(nodo.siguiente)

lista = Lista()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
print("Contar nodos:", lista.contar())
print("Sumar nodos:", lista.sumar())
print("Buscar 20:", lista.buscar(20))
print("Mostrar lista:")
lista.mostrar()
