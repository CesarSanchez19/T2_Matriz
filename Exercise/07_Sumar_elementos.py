
""" 
# Ejercicio 7 .- Obtener la suma de los elementos de una matriz.

HECHO POR AARON SANTOS ABSALÓN - COMPLETADO
"""

def suma_elementos_matriz(matriz):
    suma = 0
    for fila in matriz:
        for num in fila:
            suma += num
    return suma

# Solicitar entrada del usuario para la matriz
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

# Crear la matriz a partir de la entrada del usuario
matriz = []
print("Ingrese los elementos de la matriz fila por fila, separados por espacios:")
for _ in range(filas):
    fila = list(map(int, input().split()))
    while len(fila) != columnas:
        print(f"Error: Debes ingresar exactamente {columnas} números.")
        fila = list(map(int, input().split()))
    matriz.append(fila)

# Calcular y mostrar la suma de los elementos de la matriz
print("La suma de los elementos de la matriz es:", suma_elementos_matriz(matriz))
