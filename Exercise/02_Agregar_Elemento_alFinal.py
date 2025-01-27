# Ejercicio 2 .- Agregar un elemento al final de un arreglo (sin usar append)

# Crear matriz (array bidimensional) y ingresar manualmente los elementos.
def crear_matriz():
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("\n Ingrese los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(int, input(f"\t Ingrese los {columnas} números de la fila {i+1}, separados por espacios: ").split()))
        matriz += [fila]  # Agregar fila sin usar append
    return matriz

# Función para agregar un nuevo elemento al final de una fila en la matriz
# Función para agregar un nuevo elemento al final de una fila en la matriz
def agregar_elemento_matriz(matriz, new_elemento, fila_destino):
    # Validar que la fila destino esté dentro del rango válido
    while fila_destino < 1 or fila_destino > len(matriz):
        print("\n Está fuera de rango definido en la fila. Inténtelo nuevamente.")
        fila_destino = int(input("\t Ingrese la fila donde desea agregar el nuevo elemento: "))
    
    # Ajustar fila destino al índice correcto (índice base 0)
    fila_destino -= 1

    # Agregar el nuevo elemento al final de la fila (sin usar append)
    matriz[fila_destino] += [new_elemento]

    return matriz

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    print("\n ## Matriz actual:")
    for fila in matriz:
        print(fila)

# Programa principal
print("### Crear matriz inicial ###")
matriz = crear_matriz()  # Crear y almacenar la matriz inicial
mostrar_matriz(matriz)  # Mostrar la matriz inicial

# Pedir al usuario el elemento a agregar y la fila destino
nuevo_elemento = int(input("\n Ingrese el elemento que desea agregar: "))
fila_destino = int(input("\n Ingrese la fila donde desea agregar el nuevo elemento: "))

# Actualizar la matriz con el nuevo elemento
matriz = agregar_elemento_matriz(matriz, nuevo_elemento, fila_destino)
mostrar_matriz(matriz)  # Mostrar la matriz actualizada