"""
═══════════════════════════════════════════════════════════════════════════════
                        QUIZ 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN A
                    Sistema de Historial de Navegador Web
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Google Chrome te ha contratado para implementar el historial de navegación.
Debes diseñar e implementar el sistema usando listas enlazadas.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Pagina) con los atributos necesarios
2. Diseñar la clase Lista (Historial) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
-------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Pagina):
   - Debe almacenar: URL, título de la página, tiempo en segundos
   - Debe poder enlazarse con otra página
   
b) Clase LISTA (Historial):
   - Debe mantener referencia al inicio de la lista
   - Las páginas más recientes van al INICIO


PUNTO 2 (0.75): AGREGAR PÁGINA
------------------------------
Implementa un método para agregar una nueva página visitada.
- La página más reciente debe quedar al INICIO de la lista
- Complejidad esperada: O(1)


PUNTO 3 (1.0): TIEMPO TOTAL - RECURSIVO
---------------------------------------
Implementa un método que calcule el tiempo total de navegación.
- OBLIGATORIO usar recursividad
- Retorna la suma de segundos de todas las páginas

Ejemplo:
    Si hay páginas con tiempos [30, 120, 45] segundos
    Debe retornar 195


PUNTO 4 (1.0): BUSCAR POR DOMINIO - RECURSIVO
---------------------------------------------
Implementa un método que retorne una NUEVA lista con páginas
que contengan cierto texto en su URL.
- OBLIGATORIO usar recursividad
- No modificar la lista original

Ejemplo:
    buscar_por_dominio("youtube") 
    Retorna nueva lista con páginas cuya URL contiene "youtube"


PUNTO 5 (1.25): ELIMINAR PÁGINAS RÁPIDAS - RECURSIVO
----------------------------------------------------
Implementa un método que elimine páginas donde el usuario
estuvo menos de X segundos (probablemente clicks accidentales).
- OBLIGATORIO usar recursividad
- Modificar la lista original

Ejemplo:
    eliminar_rapidas(10)
    Elimina todas las páginas con tiempo < 10 segundos

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""
class Pagina:
    def __init__(self, titulo, url, tiempo):
        self.titulo = titulo
        self.url = url
        self.tiempo = tiempo
        self.siguiente = None

class Historial:
    def __init__(self):
        self.inicio= None

    def visitar(self, url, titulo, tiempo):
        pagina=Pagina(titulo, url, tiempo)
        pagina.siguiente= self.inicio
        self.inicio= pagina

    def tiempo_total(self):
        return self._tiempo_total_rec(self.inicio)

    def _tiempo_total_rec(self, nodo):
        if nodo is None:
            return 0
        return nodo.tiempo + self._tiempo_total_rec(nodo.siguiente)
    
    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Historial vacío")
            return

        while actual:
            print(f"🔗 {actual.titulo} | {actual.url} | {actual.tiempo}s")
            actual = actual.siguiente
    
    def buscar_por_dominio(self, texto, nodo=None, nueva_lista=None):
        # PRIMERA LLAMADA (desde el usuario)
        if nodo is None and nueva_lista is None:
            nueva_lista = Historial()
            nodo = self.inicio

        # CASO BASE: no hay más nodos
        if nodo is None:
            return nueva_lista

        # Si la URL contiene el texto buscado
        if texto.lower() in nodo.url.lower():
            nueva_lista.visitar(nodo.url, nodo.titulo, nodo.tiempo)

        # LLAMADA RECURSIVA con el siguiente nodo
        return self.buscar_por_dominio(texto, nodo.siguiente, nueva_lista)
    
    """def buscar_por_dominio(self, texto):
        nueva_lista = Historial()
        self._buscar_rec(self.inicio, texto, nueva_lista)
        return nueva_lista

    def _buscar_rec(self, nodo, texto, nueva_lista):
        if nodo is None:
            return

        if texto.lower() in nodo.url.lower():
            nueva_lista.visitar(nodo.url, nodo.titulo, nodo.tiempo)

        self._buscar_rec(nodo.siguiente, texto, nueva_lista)"""
  
    
       
    def eliminar_rapidas(self, minimo, nodo=None, primera=True):
        if primera:
            self.inicio = self.eliminar_rapidas(minimo, self.inicio, False)
            return self.inicio

        if nodo is None:
            return None

        nodo.siguiente = self.eliminar_rapidas(minimo, nodo.siguiente, False)

        if nodo.tiempo < minimo:
            return nodo.siguiente

        return nodo

# PUNTO 1a: Clase Nodo (Pagina)
# TODO: Diseñar e implementar


# PUNTO 1b: Clase Lista (Historial)
# TODO: Diseñar e implementar con los métodos de los puntos 2-5


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# (Descomenta cuando tengas tu implementación lista)
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    print("=" * 60)
    print("         PRUEBAS DEL HISTORIAL DE NAVEGACIÓN")
    print("=" * 60)
    
    # Crear historial
    historial = Historial()
    
    # Agregar páginas (la más reciente queda primero)
    historial.visitar("https://www.google.com/search", "Búsqueda Google", 15)
    historial.visitar("https://www.youtube.com/watch", "Video YouTube", 300)
    historial.visitar("https://www.github.com/repo", "GitHub Repo", 180)
    historial.visitar("https://www.youtube.com/home", "YouTube Home", 45)
    historial.visitar("https://www.google.com/maps", "Google Maps", 5)
    
    print("\\n📋 Historial inicial:")
    historial.mostrar()  # Implementa este método para visualizar
    
    # Prueba tiempo total
    print("\\n⏱️ Tiempo total:", historial.tiempo_total(), "segundos")
    print("   Esperado: 545 segundos")
    
    # Prueba buscar por dominio
    print("\\n🔍 Páginas de YouTube:")
    youtube = historial.buscar_por_dominio("youtube")
    youtube.mostrar()
    
    # Prueba eliminar rápidas
    print("\\n🗑️ Eliminando páginas < 30 segundos...")
    historial.eliminar_rapidas(30)
    historial.mostrar()
    print("   (Google Maps y Búsqueda Google deberían estar eliminadas)")