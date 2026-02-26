"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    EJERCICIO COMPLETO — BÚSQUEDAS                           ║
║                     Sistema de Gestión de Películas                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

CONTEXTO:
---------
Una plataforma de streaming necesita gestionar su catálogo de películas.
Cada película tiene: titulo, director, duracion (minutos), año (int), vista (True/False)

LISTA DOBLEMENTE LIGADA ordenada por duracion (mayor primero)

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0) — ESTRUCTURAS:
    Diseñá las clases Pelicula y Catalogo.
    - Doble ligada con anterior y siguiente
    - Ordenadas por duracion (mayor primero)

PUNTO 2 (1.0) — AGREGAR ORDENADO (recursivo):
    Ejemplo:
        Lista: [180, 120, 90]
        Agrego 150 → [180, 150, 120, 90]
        OJO: actualizar anterior Y siguiente

PUNTO 3 (0.5) — BUSCAR SI EXISTE (recursivo):
    Dado un titulo, retorná True si existe, False si no.
    Ejemplo:
        catalogo.existe("Inception") → True

PUNTO 4 (0.5) — BUSCAR PELICULA (recursivo):
    Dado un titulo, retorná el NODO completo o None si no existe.
    Ejemplo:
        pelicula = catalogo.buscar("Inception")
        print(pelicula.duracion) → 148

PUNTO 5 (0.75) — BUSCAR MAXIMA DURACION (recursivo):
    Retorná la duración de la película más larga.
    Ejemplo:
        catalogo.duracion_maxima() → 210

PUNTO 6 (0.75) — BUSCAR POR RANGO DE DURACION (recursivo):
    Retorná una NUEVA lista con películas cuya duración
    esté entre minimo y maximo (inclusive), que NO estén vistas.
    Ejemplo:
        medianas = catalogo.buscar_por_rango(90, 150)

PUNTO 7 (0.75) — CONTAR VISTAS POR DIRECTOR (recursivo):
    Contá cuántas películas YA VISTAS hay de un director dado.
    Ejemplo:
        catalogo.contar_vistas("Nolan") → 2

PUNTO 8 (0.5) — LEN PROPIO (recursivo):
    Implementá __len__ para poder usar len(catalogo).
    Ejemplo:
        len(catalogo) → 5

PUNTO 9 (0.5) — CONTAINS PROPIO (recursivo):
    Implementá __contains__ para poder usar "titulo" in catalogo.
    Ejemplo:
        "Inception" in catalogo → True

PUNTO 10 (1.25) — LIMPIAR VISTAS (recursivo):
    Eliminá todas las películas ya vistas de la lista original.
    OJO: actualizar anterior Y siguiente correctamente.

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""


class Pelicula:
    pass   # completá vos


class Catalogo:
    pass   # completá vos


if __name__ == "__main__":
    catalogo = Catalogo()

    # Agregar películas
    catalogo.agregar("Inception", "Nolan", 148, 2010)
    catalogo.agregar("El Padrino", "Coppola", 175, 1972)
    catalogo.agregar("Interstellar", "Nolan", 169, 2014)
    catalogo.agregar("Toy Story", "Lasseter", 81, 1995)
    catalogo.agregar("Avengers", "Russo", 120, 2019)

    catalogo.mostrar()
    # Esperado: El Padrino(175) > Interstellar(169) > Inception(148) > Avengers(120) > Toy Story(81)

    # PUNTO 3 — existe
    print(catalogo.existe("Inception"))      # True
    print(catalogo.existe("Batman"))         # False

    # PUNTO 4 — buscar nodo
    p = catalogo.buscar("Inception")
    print(p.duracion)                        # 148

    # PUNTO 5 — duración máxima
    print(catalogo.duracion_maxima())        # 175

    # PUNTO 6 — por rango
    medianas = catalogo.buscar_por_rango(100, 160)
    medianas.mostrar()
    # Esperado: Inception(148) y Avengers(120)

    # PUNTO 7 — contar vistas por director
    catalogo.marcar_vista("Inception")
    catalogo.marcar_vista("Interstellar")
    print(catalogo.contar_vistas("Nolan"))   # 2

    # PUNTO 8 — len
    print(len(catalogo))                     # 5

    # PUNTO 9 — contains
    print("Inception" in catalogo)           # True
    print("Batman" in catalogo)              # False

    # PUNTO 10 — limpiar vistas
    catalogo.limpiar_vistas()
    catalogo.mostrar()
    # Esperado: El Padrino, Avengers, Toy Story