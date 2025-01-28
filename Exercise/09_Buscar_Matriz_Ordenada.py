# Ejercicio 9 .- Buscar en una matriz ordenada​.

def buscar_matriz(matriz, elemento):
    for i, fila in enumerate(matriz):
        if elemento in fila:
            j = fila.index(elemento)
            return (i, j) #Retorna la posicion como (fila y columna)
    return -1, -1 #retornara -1 -1 si no esta el elemento 
    
#matriz
matriz = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 0]
]

print("Matriz: ")
for fila in matriz:
    print(fila)
    
#inserccion de datos
elemento = int(input("Ingresa el elemento a buscar: "))
fila, columna = buscar_matriz(matriz, elemento)

if fila != -1:
    print(f"El elemento {elemento} se encuentra en la posicion ({fila}, {columna}).")
else:
    print(f"El elemento {elemento} no esta en la matriz. ") 

### Hecho por Yair Gamaliel Guzman Perez