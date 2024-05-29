import machine
import utime

# Configurar pines para filas y columnas (4 filas, 3 columnas)
filas = [machine.Pin(i, machine.Pin.OUT) for i in (16, 17, 18, 19)]
columnas = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in (20, 21, 22)]

# Definir matrices de sonidos para cada instrumento
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

# Lista de nombres de instrumentos
nombres_instrumentos = ["Guitarra", "Tambor", "Batería", "Caja de haija", "Charango"]

# Inicialmente usamos el instrumento guitarra
valores_matriz = guitarra
instrumentos = [guitarra, tambor, bateria, caja_de_haija, charango]
instrumento_actual = 0

def matriz_estado():
    global valores_matriz, instrumento_actual
    instrumento_actual = (instrumento_actual + 1) % len(instrumentos)
    valores_matriz = instrumentos[instrumento_actual]
    print(f"Cambiado a {nombres_instrumentos[instrumento_actual]}")

def escanear_botones():
    for i, fila in enumerate(filas):
        fila.low()  # Activar la fila actual (baja)
        for j, columna in enumerate(columnas):
            if not columna.value():  # Si la columna está baja, el botón está presionado
                valor = valores_matriz[i][j]
                if valor == "0":
                    print(f"Botón de cambio presionado: ({i}, {j}), Valor: {valor}")
                    matriz_estado()
                else:
                    print(f"Botón presionado: ({i}, {j}), Valor: {valor}")
                while not columna.value():  # Esperar a que se libere el botón
                    utime.sleep_ms(10)
        fila.high()  # Desactivar la fila actual (alta)

while True:
    escanear_botones()
    utime.sleep_ms(100)