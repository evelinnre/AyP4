# ═══════════════════════════════════════════════════════════════════════════════
# QUIZ 1 - ESTRUCTURAS DE DATOS
# EXAMEN E
# Sistema de Gestión de Cuentas Bancarias
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 1a: Clase Nodo (Cuenta)
class Cuenta:
    def __init__(self, numero, titular, saldo, activa=True):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.activa = activa
        self.siguiente = None


# PUNTO 1b: Clase Lista (Banco)
class Banco:
    def __init__(self):
        self.inicio = None

    # PUNTO 2: Agregar cuenta al inicio (O(1))
    def agregar_cuenta(self, numero, titular, saldo, activa=True):
        nueva = Cuenta(numero, titular, saldo, activa)
        nueva.siguiente = self.inicio
        self.inicio = nueva

    # Método auxiliar para mostrar cuentas
    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("No hay cuentas registradas")
            return
        while actual:
            estado = "✓" if actual.activa else "✗"
            print(f"[{estado}] Cuenta {actual.numero} - {actual.titular} - ${actual.saldo}")
            actual = actual.siguiente

    # PUNTO 3: Calcular saldo total (recursivo)
    def saldo_total(self):
        return self._saldo_total_rec(self.inicio)

    def _saldo_total_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.saldo + self._saldo_total_rec(nodo.siguiente)

    # PUNTO 4: Buscar cuentas activas (recursivo)
    def buscar_activas(self):
        nueva = Banco()
        self._buscar_activas_rec(self.inicio, nueva)
        return nueva

    def _buscar_activas_rec(self, nodo, nueva_lista):
        if nodo is None:
            return
        if nodo.activa:
            nueva_lista.agregar_cuenta(
                nodo.numero, nodo.titular, nodo.saldo, nodo.activa
            )
        self._buscar_activas_rec(nodo.siguiente, nueva_lista)

    # PUNTO 5: Eliminar cuentas inactivas (recursivo)
    def eliminar_inactivas(self):
        self.inicio = self._eliminar_inactivas_rec(self.inicio)

    def _eliminar_inactivas_rec(self, nodo):
        if nodo is None:
            return None
        if not nodo.activa:
            return self._eliminar_inactivas_rec(nodo.siguiente)
        nodo.siguiente = self._eliminar_inactivas_rec(nodo.siguiente)
        return nodo


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL SISTEMA BANCARIO")
    print("=" * 60)

    banco = Banco()

    banco.agregar_cuenta(1001, "Ana Pérez", 2500, True)
    banco.agregar_cuenta(1002, "Luis Gómez", 1200, False)
    banco.agregar_cuenta(1003, "María Torres", 5000, True)
    banco.agregar_cuenta(1004, "Carlos Ruiz", 800, False)
    banco.agregar_cuenta(1005, "Sofía López", 3000, True)

    print("\n🏦 Cuentas registradas:")
    banco.mostrar()

    print("\n💰 Saldo total del banco:", banco.saldo_total())
    print("   Esperado: 12500")

    print("\n🔍 Cuentas activas:")
    cuentas_activas = banco.buscar_activas()
    cuentas_activas.mostrar()

    print("\n🗑️ Eliminando cuentas inactivas...")
    banco.eliminar_inactivas()
    banco.mostrar()