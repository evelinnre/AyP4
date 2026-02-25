def busqueda_binaria(lista, valor, inicio, fin):
    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2

    if lista[medio] == valor:
        return medio
    elif valor < lista[medio]:
        return busqueda_binaria(lista, valor, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, valor, medio + 1, fin)
    
lista = [1, 3, 5, 7, 9]
print(busqueda_binaria(lista, 7, 0, len(lista) - 1))