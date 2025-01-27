# Ejercicio 1 - Eliminar un elemento de una matriz (sin usar del, remove, pop)

### Hecho por Cesar David Sanchez Trejo

# Crear matriz (array bidimensional) y ingresar manualmente los elementos.
def crear_matriz():
    print("\n ### Creando una Matriz:")
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    matriz = []
    print("\n Ingrese los elementos de la matriz fila por fila:")
    for i in range(filas):
        fila = list(map(int, input(f"\t Ingrese los {columnas} números de la fila {i+1}, separados por espacios: ").split()))
        matriz += [fila]  # Agregar fila sin usar append
    return matriz

# Función para eliminar un elemento de la matriz
def deleted_element(matriz, del_element):
    nueva_matriz = []
    
    for fila in matriz:
        nueva_fila = [elemento for elemento in fila if elemento != del_element]
        nueva_matriz += [nueva_fila]
    
    return nueva_matriz

# Crear matriz y mostrarla
matriz = crear_matriz()
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario el número que desea eliminar
del_element = int(input("\t Ingrese el número que desea eliminar: "))

# Eliminar elemento y mostrar resultado
matriz_resultado = deleted_element(matriz, del_element)
print("\t Matriz después de eliminar el elemento:")
for fila in matriz_resultado:
    print(fila)