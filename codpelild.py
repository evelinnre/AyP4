# ============================================================
# PUNTO 1 — ESTRUCTURAS
# ============================================================

class Pelicula:
    def __init__(self, titulo, director, duracion, año):
        self.titulo    = titulo
        self.director  = director
        self.duracion  = duracion
        self.año       = año
        self.vista     = False
        self.anterior  = None
        self.siguiente = None

    def __str__(self):
        estado = "✓" if self.vista else "○"
        return f"[{estado}] {self.titulo} | Dir: {self.director} | {self.duracion} min | {self.año}"


class Catalogo:
    def __init__(self):
        self.cabeza = None

    # ──────────────────────────────────────────────────────
    # PUNTO 2 — AGREGAR ORDENADO (recursivo)
    # ──────────────────────────────────────────────────────

    def agregar(self, titulo, director, duracion, año):
        nueva = Pelicula(titulo, director, duracion, año)
        self.cabeza = self._agregar_recursivo(self.cabeza, nueva, None)

    def _agregar_recursivo(self, nodo, nueva, previo):
        # Caso base: lista vacía o encontramos la posición
        if nodo is None or nueva.duracion > nodo.duracion:
            nueva.anterior  = previo
            nueva.siguiente = nodo
            if nodo:
                nodo.anterior = nueva       # actualizamos el anterior del desplazado
            if previo:
                previo.siguiente = nueva    # actualizamos el siguiente del previo
            return nueva if previo is None else self.cabeza

        # Caso recursivo
        self._agregar_recursivo(nodo.siguiente, nueva, nodo)
        return self.cabeza                  # siempre devolvemos la cabeza real

    # ──────────────────────────────────────────────────────
    # PUNTO 3 — BUSCAR SI EXISTE (recursivo)
    # ──────────────────────────────────────────────────────

    def existe(self, titulo):
        return self._existe_recursivo(self.cabeza, titulo)

    def _existe_recursivo(self, nodo, titulo):
        if nodo is None:
            return False
        if nodo.titulo == titulo:
            return True
        return self._existe_recursivo(nodo.siguiente, titulo)

    # ──────────────────────────────────────────────────────
    # PUNTO 4 — BUSCAR NODO (recursivo)
    # ──────────────────────────────────────────────────────

    def buscar(self, titulo):
        return self._buscar_recursivo(self.cabeza, titulo)

    def _buscar_recursivo(self, nodo, titulo):
        if nodo is None:
            return None
        if nodo.titulo == titulo:
            return nodo
        return self._buscar_recursivo(nodo.siguiente, titulo)

    # ──────────────────────────────────────────────────────
    # PUNTO 5 — DURACIÓN MÁXIMA (recursivo)
    # ──────────────────────────────────────────────────────

    def duracion_maxima(self):
        if self.cabeza is None:
            return 0
        return self._max_recursivo(self.cabeza)

    def _max_recursivo(self, nodo):
        # Caso base: último nodo
        if nodo.siguiente is None:
            return nodo.duracion
        return max(nodo.duracion, self._max_recursivo(nodo.siguiente))

    # ──────────────────────────────────────────────────────
    # PUNTO 6 — BUSCAR POR RANGO (recursivo)
    # ──────────────────────────────────────────────────────

    def buscar_por_rango(self, minimo, maximo):
        nuevo_catalogo = Catalogo()
        self._rango_recursivo(self.cabeza, minimo, maximo, nuevo_catalogo)
        return nuevo_catalogo

    def _rango_recursivo(self, nodo, minimo, maximo, nuevo_catalogo):
        if nodo is None:
            return
        if minimo <= nodo.duracion <= maximo and not nodo.vista:
            nuevo_catalogo.agregar(nodo.titulo, nodo.director, nodo.duracion, nodo.año)
        self._rango_recursivo(nodo.siguiente, minimo, maximo, nuevo_catalogo)

    # ──────────────────────────────────────────────────────
    # PUNTO 7 — CONTAR VISTAS POR DIRECTOR (recursivo)
    # ──────────────────────────────────────────────────────

    def contar_vistas(self, director):
        return self._contar_recursivo(self.cabeza, director)

    def _contar_recursivo(self, nodo, director):
        if nodo is None:
            return 0
        coincide = 1 if (nodo.director == director and nodo.vista) else 0
        return coincide + self._contar_recursivo(nodo.siguiente, director)

    # ──────────────────────────────────────────────────────
    # PUNTO 8 — LEN (recursivo)
    # ──────────────────────────────────────────────────────

    def __len__(self):
        return self._len_recursivo(self.cabeza)

    def _len_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._len_recursivo(nodo.siguiente)

    # ──────────────────────────────────────────────────────
    # PUNTO 9 — CONTAINS (recursivo)
    # ──────────────────────────────────────────────────────

    def __contains__(self, titulo):
        return self._existe_recursivo(self.cabeza, titulo)  # reutilizamos punto 3

    # ──────────────────────────────────────────────────────
    # PUNTO 10 — LIMPIAR VISTAS (recursivo)
    # ──────────────────────────────────────────────────────

    def limpiar_vistas(self):
        self.cabeza = self._limpiar_recursivo(self.cabeza)
        if self.cabeza:
            self.cabeza.anterior = None     # aseguramos que la nueva cabeza no tenga previo

    def _limpiar_recursivo(self, nodo):
        if nodo is None:
            return None
        nodo.siguiente = self._limpiar_recursivo(nodo.siguiente)
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo  # actualizamos el puntero anterior
        if nodo.vista:
            return nodo.siguiente           # saltamos el nodo visto
        return nodo

    # ──────────────────────────────────────────────────────
    # UTILIDAD
    # ──────────────────────────────────────────────────────

    def marcar_vista(self, titulo):
        nodo = self.buscar(titulo)
        if nodo:
            nodo.vista = True

    def mostrar(self):
        nodo = self.cabeza
        if nodo is None:
            print("  (catálogo vacío)")
            return
        partes = []
        while nodo:
            partes.append(f"{nodo.titulo}({nodo.duracion})")
            nodo = nodo.siguiente
        print(" > ".join(partes))


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    catalogo = Catalogo()

    catalogo.agregar("Inception",    "Nolan",    148, 2010)
    catalogo.agregar("El Padrino",   "Coppola",  175, 1972)
    catalogo.agregar("Interstellar", "Nolan",    169, 2014)
    catalogo.agregar("Toy Story",    "Lasseter",  81, 1995)
    catalogo.agregar("Avengers",     "Russo",    120, 2019)

    print("=== Catálogo inicial ===")
    catalogo.mostrar()
    # El Padrino(175) > Interstellar(169) > Inception(148) > Avengers(120) > Toy Story(81)

    print("\n=== PUNTO 3 — existe ===")
    print(catalogo.existe("Inception"))   # True
    print(catalogo.existe("Batman"))      # False

    print("\n=== PUNTO 4 — buscar nodo ===")
    p = catalogo.buscar("Inception")
    print(p.duracion)                     # 148

    print("\n=== PUNTO 5 — duración máxima ===")
    print(catalogo.duracion_maxima())     # 175

    print("\n=== PUNTO 6 — por rango (100–160) ===")
    medianas = catalogo.buscar_por_rango(100, 160)
    medianas.mostrar()
    # Inception(148) > Avengers(120)

    print("\n=== PUNTO 7 — contar vistas Nolan ===")
    catalogo.marcar_vista("Inception")
    catalogo.marcar_vista("Interstellar")
    print(catalogo.contar_vistas("Nolan"))  # 2

    print("\n=== PUNTO 8 — len ===")
    print(len(catalogo))                    # 5

    print("\n=== PUNTO 9 — contains ===")
    print("Inception" in catalogo)          # True
    print("Batman" in catalogo)             # False

    print("\n=== PUNTO 10 — limpiar vistas ===")
    catalogo.limpiar_vistas()
    catalogo.mostrar()
    # El Padrino(175) > Avengers(120) > Toy Story(81)