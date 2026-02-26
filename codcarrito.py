"""Una tienda online necesita gestionar su carrito de compras.
Cada producto tiene: nombre, precio (float), cantidad (int), agregado (True/False)

PUNTO 1 - ESTRUCTURAS:
Diseñá las clases Producto y Carrito.
Los productos se mantienen ordenados por precio (mayor primero).

PUNTO 2 - AGREGAR ORDENADO (recursivo):
Agregá un producto en la posición correcta según precio.

Ejemplo:
  Lista: [1000, 500, 200]
  Agrego 750 → [1000, 750, 500, 200]

PUNTO 3 - CALCULAR TOTAL (recursivo):
Calculá el precio total sumando precio * cantidad de cada producto.

Ejemplo:
  calcular_total() → 3500.0

PUNTO 4 - OBTENER CAROS (recursivo):
Retorná una NUEVA lista con productos de precio mayor a un máximo dado
que NO hayan sido agregados aún.

Ejemplo:
  caros = carrito.obtener_caros(500)

PUNTO 5 - LIMPIAR AGREGADOS (recursivo):
Eliminá todos los productos ya agregados de la lista original.

  Antes:  [✓]Producto1 -> [○]Producto2 -> [✓]Producto3
  Después: [○]Producto2"""

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio  # 1 (baja) a 5 (urgente)
        self.cantidad = cantidad
        self.agregado = False
        self.siguiente = None
class Carrito:
    def __init__(self):
        self.inicio = None

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo=Producto(nombre, precio, cantidad)
        if self.inicio is None or self.inicio.precio<nuevo.precio:
            nuevo.siguiente= self.inicio
            self.inicio= nuevo
        else:
            self._agregar_producto(self.inicio, nuevo)
            
    def _agregar_producto(self,nodo,nuevo):
        if nodo.siguiente is None or nodo.siguiente.precio<nuevo.precio:
            nuevo.siguiente=nodo.siguiente
            nodo.siguiente=nuevo
        else:
            self._agregar_producto(nodo.siguiente, nuevo)
            
    def calcular_total(self):
        return self._calcular_total_rec(self.inicio)
        
    def _calcular_total_rec(self,nodo):
        if nodo is None:
            return 0
        return (nodo.precio*nodo.cantidad)+self._calcular_total_rec(nodo.siguiente)
        
    def obtener_caros(self, maximo):
        nueva_lista= Carrito()
        return self._obtener_caros(self.inicio, nueva_lista, maximo)
        
        
    def _obtener_caros(self, nodo, lista, maximo):
        if nodo is None:
            return lista
        if nodo.precio > maximo:
            lista.agregar_producto(nodo.nombre, nodo.precio, nodo.cantidad)
        return self._obtener_caros(nodo.siguiente, lista, maximo) 
        
    def limpiar_agregados(self):
        self.inicio= self._limpiar_rec(self.inicio)
        
    def _limpiar_rec(self,nodo):
        if nodo is None:
            return None
        if nodo.agregado:
            return self._limpiar_rec(nodo.siguiente)
        nodo.siguiente=self._limpiar_rec(nodo.siguiente)
        return nodo
        
    def mostrar(self):
        actual=self.inicio
        
        if actual is None:
            print("carrito vacío")
            return

        while actual:
            print(f"🔗 {actual.nombre} | {actual.precio} | {actual.cantidad}")
            actual = actual.siguiente
            
    def marcar_agregado(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.agregado = True
                return
            actual = actual.siguiente
        
        
if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL CARRITO DE COMPRAS")
    print("=" * 60)

    carrito = Carrito()

    # PRUEBA 1 - agregar ordenado por precio
    print("\n--- PRUEBA 1: Agregar productos ordenados por precio ---")
    carrito.agregar_producto("jabon", 1000, 1)
    carrito.agregar_producto("shampoo", 12000, 2)
    carrito.agregar_producto("acondicionador", 23000, 1)
    carrito.agregar_producto("crema", 8000, 3)
    carrito.mostrar()
    # Esperado: acondicionador(23000) > shampoo(12000) > crema(8000) > jabon(1000)

    # PRUEBA 2 - calcular total
    print("\n--- PRUEBA 2: Calcular total ---")
    total = carrito.calcular_total()
    print(f"Total: ${total}")
    # Esperado: 23000*1 + 12000*2 + 8000*3 + 1000*1 = 72000

    # PRUEBA 3 - marcar agregados y obtener caros
    print("\n--- PRUEBA 3: Obtener caros (> $10000) sin agregar ---")
    carrito.marcar_agregado("acondicionador")  # este NO debe aparecer (agregado)
    caros = carrito.obtener_caros(10000)
    caros.mostrar()
    # Esperado: solo shampoo(12000), acondicionador fue marcado

    # PRUEBA 4 - limpiar agregados
    print("\n--- PRUEBA 4: Limpiar agregados ---")
    print("Antes:")
    carrito.mostrar()
    carrito.marcar_agregado("jabon")
    carrito.limpiar_agregados()
    print("Después:")
    carrito.mostrar()
    # Esperado: acondicionador y jabon eliminados, quedan shampoo y crema

    # PRUEBA 5 - carrito vacío
    print("\n--- PRUEBA 5: Limpiar todo ---")
    carrito.marcar_agregado("shampoo")
    carrito.marcar_agregado("crema")
    carrito.limpiar_agregados()
    carrito.mostrar()
    # Esperado: carrito vacío