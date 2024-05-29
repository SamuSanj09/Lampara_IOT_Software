# Matriz de valores
valor_matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def manejo_matriz(valor):
    for i in range(len(valor_matriz)):
        for j in range(len(valor_matriz[i])):
            valor_matriz[i][j] = valor
    for fila in valor_matriz:
        print(fila)
