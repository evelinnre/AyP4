# ============================================================
# PUNTO 1 - ESTRUCTURAS
# ============================================================

class Paciente:
    def __init__(self, nombre, edad, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.gravedad = gravedad
        self.atendido = False
        self.siguiente = None  # para lista enlazada

    def __str__(self):
        estado = "✓" if self.atendido else "○"
        return f"[{estado}] {self.nombre} (edad: {self.edad}, gravedad: {self.gravedad})"


class SalaEspera:
    def __init__(self):
        self.cabeza = None  # lista enlazada ordenada por gravedad

    # ============================================================
    # PUNTO 2 - AGREGAR ORDENADO (recursivo)
    # ============================================================

    def agregar_paciente(self, paciente):
        """Inserta un paciente en la posición correcta según gravedad (mayor primero)."""
        self.cabeza = self._agregar_recursivo(self.cabeza, paciente)

    def _agregar_recursivo(self, nodo_actual, paciente):
        # Caso base: lista vacía o encontramos la posición correcta
        if nodo_actual is None or paciente.gravedad > nodo_actual.gravedad:
            paciente.siguiente = nodo_actual
            return paciente
        # Caso recursivo: seguimos buscando la posición
        nodo_actual.siguiente = self._agregar_recursivo(nodo_actual.siguiente, paciente)
        return nodo_actual

    # ============================================================
    # PUNTO 3 - CONTAR POR GRAVEDAD (recursivo)
    # ============================================================

    def contar_graves(self, gravedad):
        """Cuenta cuántos pacientes NO atendidos tienen cierta gravedad."""
        return self._contar_recursivo(self.cabeza, gravedad)

    def _contar_recursivo(self, nodo, gravedad):
        # Caso base: lista vacía
        if nodo is None:
            return 0
        # Sumo 1 si coincide la gravedad y no fue atendido
        coincide = 1 if (nodo.gravedad == gravedad and not nodo.atendido) else 0
        return coincide + self._contar_recursivo(nodo.siguiente, gravedad)

    # ============================================================
    # PUNTO 4 - OBTENER CRÍTICOS (recursivo)
    # ============================================================

    def obtener_criticos(self):
        """Retorna una nueva lista con pacientes de gravedad 4 o 5 no atendidos."""
        nueva_sala = SalaEspera()
        nueva_sala.cabeza = self._criticos_recursivo(self.cabeza)
        return nueva_sala

    def _criticos_recursivo(self, nodo):
        # Caso base
        if nodo is None:
            return None
        resto = self._criticos_recursivo(nodo.siguiente)
        # Si es crítico y no atendido, creamos una copia y la enlazamos
        if nodo.gravedad >= 4 and not nodo.atendido:
            copia = Paciente(nodo.nombre, nodo.edad, nodo.gravedad)
            copia.atendido = nodo.atendido
            copia.siguiente = resto
            return copia
        return resto

    # ============================================================
    # PUNTO 5 - LIMPIAR ATENDIDOS (recursivo)
    # ============================================================

    def limpiar_atendidos(self):
        """Elimina todos los pacientes ya atendidos de la lista original."""
        self.cabeza = self._limpiar_recursivo(self.cabeza)

    def _limpiar_recursivo(self, nodo):
        # Caso base
        if nodo is None:
            return None
        # Procesamos el resto primero
        nodo.siguiente = self._limpiar_recursivo(nodo.siguiente)
        # Si está atendido, lo "saltamos" devolviendo su siguiente
        if nodo.atendido:
            return nodo.siguiente
        return nodo

    # ============================================================
    # UTILIDAD - Mostrar lista
    # ============================================================

    def mostrar(self):
        nodo = self.cabeza
        if nodo is None:
            print("  (sala vacía)")
        while nodo:
            print(" ", nodo)
            nodo = nodo.siguiente


# ============================================================
# PRUEBA COMPLETA
# ============================================================

sala = SalaEspera()

p1 = Paciente("Ana",    30, 5)
p2 = Paciente("Luis",   45, 3)
p3 = Paciente("Marta",  60, 1)
p4 = Paciente("Carlos", 25, 4)
p5 = Paciente("Elena",  50, 5)
p6 = Paciente("Pedro",  35, 2)

for p in [p1, p2, p3, p4, p5, p6]:
    sala.agregar_paciente(p)

print("=== Lista inicial ===")
sala.mostrar()

print("\n=== Contar gravedad 5 no atendidos ===")
print(" contar_graves(5) →", sala.contar_graves(5))

print("\n=== Marcar algunos como atendidos ===")
p1.atendido = True   # Ana  (gravedad 5) ✓
p2.atendido = True   # Luis (gravedad 3) ✓

print("\n=== Obtener críticos (gravedad 4 o 5, no atendidos) ===")
criticos = sala.obtener_criticos()
criticos.mostrar()

print("\n=== Limpiar atendidos ===")
sala.limpiar_atendidos()
sala.mostrar()


