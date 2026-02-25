def suma_lista(lista, acumulador=0):
    # Caso base
    if len(lista) == 0:
        return acumulador
    # Caso recursivo
    return suma_lista(lista[1:], lista[0] + acumulador)
lista = [2, 3]
print(suma_lista(lista))

def potencia_tail(base, exponente, acumulador=1):
    # Caso base
    if exponente == 0:
        return acumulador
    # Caso recursivo
    return potencia_tail(base, exponente - 1, acumulador * base)

lista = [2, 3]
print(potencia_tail(lista[0], lista[1]))

def potencias(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    # Caso recursivo
    return base * potencia(base, exponente - 1)

lista = [2, 3]
print(potencias(lista[0], lista[1]))

