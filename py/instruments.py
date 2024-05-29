guitarra = [
    ["Acorde G", "Acorde C", "Acorde D"],
    ["Acorde E", "Acorde Am", "Acorde Em"],
    ["Acorde F", "Rasgueo", "Punteo"],
    ["0", "0", "0"]
]

tambor = [
    ["Tambor 1", "Tambor 2", "Tambor 3"],
    ["Tambor 4", "Tambor 5", "Tambor 6"],
    ["Tambor 7", "Tambor 8", "Tambor 9"],
    ["0", "0", "0"]
]

bateria = [
    ["Bombo", "Caja", "Hi-hat"],
    ["Tom 1", "Tom 2", "Tom 3"],
    ["Bombo 2", "Caja 2", "Hi-hat 2"],
    ["0", "0", "0"]
]

caja_de_haija = [
    ["Golpe 1", "Golpe 2", "Golpe 3"],
    ["Golpe 4", "Golpe 5", "Golpe 6"],
    ["Golpe 7", "Golpe 8", "Golpe 9"],
    ["0", "0", "0"]
]

charango = [
    ["Nota G", "Nota C", "Nota D"],
    ["Nota E", "Nota A", "Nota B"],
    ["Nota F", "Rasgueo 1", "Rasgueo 2"],
    ["0", "0", "0"]
]

nombres_instrumentos = ["Guitarra", "Tambor", "Batería", "Caja de haija", "Charango"]

instrumentos = [guitarra, tambor, bateria, caja_de_haija, charango]

instrumento_actual = 0
valores_matriz = guitarra

def cambiar_instrumento():
    global valores_matriz, instrumento_actual
    instrumento_actual = (instrumento_actual + 1) % len(instrumentos)
    valores_matriz = instrumentos[instrumento_actual]
    print(f"Cambiado a {nombres_instrumentos[instrumento_actual]}")
    
def manejo_matriz(valor, valor_matriz):
    for i in range(len(valor_matriz)):
        for j in range(len(valor_matriz[i])):
            valor_matriz[i][j] = valor
    for fila in valor_matriz:
        print(fila)
