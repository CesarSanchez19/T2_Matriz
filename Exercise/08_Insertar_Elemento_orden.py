# Ejercicio 8 .- Insertar un elemento en orden en una matriz​.

def insertar_en_orden(matriz, fila, elemento):
    #aqui se verifica que la fila sea valida 
    if fila < 0 or fila >= len(matriz):
        print("Fila no valida")
        return matriz
    
    # se insertara el elemento en la posicion correcto 
    matriz[fila].append(elemento)
    matriz[fila].sort() #Mantiene el orden ascendente 
    return matriz

#matriz
matriz = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]


print("Matriz original")
for fila in matriz: 
    print(fila)

#Aqui insertaremos un nuevo elemnto a la matriz y seleccionaremos la fila 

fila = int(input("Ingresa la fila donde quieres insertar el nuevo elemento: "))
elemento = int(input("Ingrese un elemento al insertar: "))

matriz = insertar_en_orden(matriz, fila, elemento)

print("Nueva matriz: ")
for fila in matriz:
    print(fila)

### Hecho por Yair Gamaliel Guzman Perez