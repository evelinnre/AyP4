def suma_digitos(n):
    # Caso base
    if n < 10:
        return n
    # Caso recursivo
    return (n % 10) + suma_digitos(n // 10)

numero = 1503
resultado = suma_digitos(numero)
print(resultado)