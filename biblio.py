# ═══════════════════════════════════════════════════════════════════════════════
# QUIZ 1 - ESTRUCTURAS DE DATOS
# EXAMEN D
# Sistema de Gestión de Biblioteca
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 1a: Clase Nodo (Libro)
class Libro:
    def __init__(self, titulo, autor, anio, prestado=False):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = prestado
        self.siguiente = None


# PUNTO 1b: Clase Lista (Biblioteca)
class Biblioteca:
    def __init__(self):
        self.inicio = None

    # PUNTO 2: Agregar libro al inicio (O(1))
    def agregar_libro(self, titulo, autor, anio, prestado=False):
        nuevo = Libro(titulo, autor, anio, prestado)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    # Método auxiliar para mostrar
    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Biblioteca vacía")
            return
        while actual:
            estado = "✓" if actual.prestado else "○"
            print(f"[{estado}] {actual.titulo} - {actual.autor} ({actual.anio})")
            actual = actual.siguiente

    # PUNTO 3: Contar libros disponibles (recursivo)
    def contar_disponibles(self):
        return self._contar_disponibles_rec(self.inicio)

    def _contar_disponibles_rec(self, nodo):
        if nodo is None:
            return 0
        if not nodo.prestado:
            return 1 + self._contar_disponibles_rec(nodo.siguiente)
        return self._contar_disponibles_rec(nodo.siguiente)

    # PUNTO 4: Buscar por autor (recursivo)
    def buscar_por_autor(self, autor):
        nueva = Biblioteca()
        self._buscar_por_autor_rec(self.inicio, autor, nueva)
        return nueva

    def _buscar_por_autor_rec(self, nodo, autor, nueva_lista):
        if nodo is None:
            return
        if nodo.autor == autor:
            nueva_lista.agregar_libro(
                nodo.titulo, nodo.autor, nodo.anio, nodo.prestado
            )
        self._buscar_por_autor_rec(nodo.siguiente, autor, nueva_lista)

    # PUNTO 5: Eliminar libros prestados (recursivo)
    def eliminar_prestados(self):
        self.inicio = self._eliminar_prestados_rec(self.inicio)

    def _eliminar_prestados_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.prestado:
            return self._eliminar_prestados_rec(nodo.siguiente)
        nodo.siguiente = self._eliminar_prestados_rec(nodo.siguiente)
        return nodo


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA DE BIBLIOTECA")
    print("=" * 60)

    biblioteca = Biblioteca()

    biblioteca.agregar_libro("1984", "George Orwell", 1949, True)
    biblioteca.agregar_libro("El principito", "Antoine de Saint-Exupéry", 1943)
    biblioteca.agregar_libro("Rebelión en la granja", "George Orwell", 1945)
    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)
    biblioteca.agregar_libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981)

    print("\n📚 Biblioteca inicial:")
    biblioteca.mostrar()

    print("\n📊 Libros disponibles:", biblioteca.contar_disponibles())
    print("   Esperado: 3")

    print("\n🔍 Libros del autor buscado:")
    libros_autor = biblioteca.buscar_por_autor("George Orwell")
    libros_autor.mostrar()

    print("\n🗑️ Eliminando libros prestados...")
    biblioteca.eliminar_prestados()
    biblioteca.mostrar()