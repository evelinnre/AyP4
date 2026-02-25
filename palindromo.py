def es_palindroma(palabra):
    # Convertimos a minúsculas para evitar errores
    palabra = palabra.lower()
    
    # Caso base- si la palabra tiene una letra o ninguna es palindroma
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo
    if palabra[0] == palabra[-1]:      #compara la primera y ultima letra
        return es_palindroma(palabra[1:-1])   #slicing(corte de cadenas) significa que empieza en la primera letra y termina antes de la ultima
    else:
        return False

# ===== PROGRAMA PRINCIPAL =====
palabra = input("Ingrese una palabra: ")

if es_palindroma(palabra):
    print("La palabra ES palíndroma")
else:
    print("La palabra NO es palíndroma")