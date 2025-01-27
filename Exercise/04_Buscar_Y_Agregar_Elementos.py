# Ejercicio 4 .- Buscar y agregar (combinación de las dos anteriores). Se busca un elemento en el array y regresar la posición donde se encontró o si no está, agregarlo al final de la matriz.

### Hecho por Cesar David Sanchez Trejo

# Función para crear una matriz bidimensional ingresada manualmente
def crear_matriz():
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("\n ## Ingrese los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los {columnas} números de la fila {i+1}, separados por espacios: ").split()))
        matriz += [fila]  
    return matriz

# Función para agregar un nuevo elemento al final de una fila en la matriz
def agregar_elemento_matriz(matriz, new_elemento, fila_destino):
    # Validar que la fila destino esté dentro del rango válido
    while fila_destino < 1 or fila_destino > len(matriz):
        print("\n Está fuera de rango definido en la fila. Inténtelo nuevamente.")
        fila_destino = int(input("\n Ingrese la fila donde desea agregar el nuevo elemento: "))
    
    # Ajustar fila destino al índice correcto (índice base 0)
    fila_destino -= 1

    # Agregar el nuevo elemento al final de la fila (sin usar append)
    matriz[fila_destino] += [new_elemento]

    return matriz

# Función para buscar un elemento en la matriz (de manera recursiva)
def search_element_recursivo(matriz, elemento, fila=0, columna=0):
    # Caso base: si se llega al final de la matriz sin encontrar el elemento
    if fila >= len(matriz):
        return -1, -1
    
    # Caso base: si se encuentra el elemento en la posición actual
    if columna < len(matriz[fila]) and matriz[fila][columna] == elemento:
        return fila, columna
    
    # Avanzar al siguiente elemento
    if columna + 1 < len(matriz[fila]):
        return search_element_recursivo(matriz, elemento, fila, columna + 1)
    else:
        return search_element_recursivo(matriz, elemento, fila + 1, 0)

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    print("\nMatriz actual:")
    for fila in matriz:
        print(fila)

print("### Crear matriz inicial ###")
matriz = crear_matriz()  # Crear y almacenar la matriz inicial
mostrar_matriz(matriz)  # Mostrar la matriz inicial

# Solicitar el elemento a buscar
elemento = int(input("\nIngrese el elemento que desea buscar: "))

# Realizar la búsqueda recursiva
fila, columna = search_element_recursivo(matriz, elemento)

# Si el elemento fue encontrado, mostrar su posición
if fila != -1 and columna != -1:
    print(f"\t Elemento encontrado en la posición (fila {fila + 1}, columna {columna + 1}).")
else:
    print("\t Elemento no encontrado en la matriz.")
    
    # Pedir al usuario el nuevo elemento y la fila destino para agregarlo
    new_elemento = int(input("\n Ingrese el nuevo elemento que desea agregar : "))
    fila_destino = int(input("\n Ingrese la fila donde desea agregar el nuevo elemento: "))

    # Actualizar la matriz con el nuevo elemento
    matriz = agregar_elemento_matriz(matriz, new_elemento, fila_destino)
    mostrar_matriz(matriz)  # Mostrar la matriz actualizada
