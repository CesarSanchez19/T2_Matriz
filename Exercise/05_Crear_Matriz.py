
""" 
# Ejercicio 5 .- Crear una matriz de m * n e inicializar con el parámetro dado.

HECHO POR AARON SANTOS ABSALÓN - COMPLETADO
"""

def crear_matriz(m, n, valor):
    # Crear la matriz con el valor especificado
    matriz = [[valor for _ in range(n)] for _ in range(m)]
    
    # Imprimir la matriz
    for fila in matriz:
        print(fila)
    
    return matriz


# Pedir al usuario los valores necesarios

m = int(input("Escribe un número que será el num. de filas: "))  # Número de filas
n = int(input("Escribe un número que será el num. de columnas: "))  # Número de columnas
valor_inicial = int(input("Escribe un número que se mostrará en la matriz: "))  # Valor inicial

# Llamar a la función con los valores ingresados
crear_matriz(m, n, valor_inicial)