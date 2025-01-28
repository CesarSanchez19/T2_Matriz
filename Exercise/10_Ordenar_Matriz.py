# Ejercicio 10 ,- Ordenar una matriz (método burbuja).

def ordenar_matriz(matriz):
    #conversion de matriz bidimensional a una fila plana
    lista = [elemento for fila in matriz for elemento in fila]
    
    #metodo de la burbuja
    n = len(lista)
    for h in range(n):
        for y in range(0, n - h - 1):
            if lista[y] > lista[y + 1]:
                lista[y], lista[y + 1] = lista[y + 1], lista[y]
                
    #reconstruye la matriz con los elementos ordenados 
    filas = len(matriz)
    columnas = len(matriz[0])
    return [lista[h * columnas:(h + 1) * columnas] for h in range(filas)]

#impresion matriz 
matriz = [
    [3, 1, 4],
    [6, 5, 9],
    [8, 7, 2]
]

print("Matriz original: ")
for fila in matriz:
    print(fila)
    
matriz_ordenada = ordenar_matriz(matriz)

print("\Matriz ordenada: ")
for fila in matriz_ordenada:
    print(fila)  
                
                

### Hecho por Yair Gamaliel Guzman Perez