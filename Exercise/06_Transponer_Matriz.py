
""" 
Ejericio 6 .- Transponer una matriz (intercambiar filas por columnas).

HECHO POR AARON SANTOS ABSALÓN - COMPLETADO
"""

def transponer_matriz(matriz):
    # Usando comprensión de listas para transponer la matriz
    matriz_transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return matriz_transpuesta

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

# Transponer la matriz
matriz_transpuesta = transponer_matriz(matriz)

# Mostrar la matriz transpuesta
print("La matriz transpuesta es:")
for fila in matriz_transpuesta:
    print(fila)
