# Ejercicio 3.- Búsqueda de un elemento en una matriz bidimensional (recursiva o iterativa).

# Hecho por Cesar David Sanchez Trejo

# Solicitar al usuario que ingrese los elementos de la matriz
def crear_matriz():
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("\n ## Ingrese los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los {columnas} números de la fila {i+1}, separados por espacios: ").split()))
        matriz += [fila]  
    return matriz

# Función para búsqueda recursiva en una matriz bidimensional
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
    print("\n Matriz ingresada:")
    for fila in matriz:
        print(fila)

# Programa principal
print("### Crear matriz inicial ###")
matriz = crear_matriz()
mostrar_matriz(matriz)

# Solicitar el elemento a buscar
elemento = int(input("\t Ingrese el elemento que desea buscar: "))

# Realizar la búsqueda recursiva
fila, columna = search_element_recursivo(matriz, elemento)

# Mostrar el resultado
if fila != -1 and columna != -1:
    print(f"\n Elemento encontrado en la posición (fila {fila + 1}, columna {columna + 1}).")
else:
    print("\n Elemento no encontrado en la matriz.")
