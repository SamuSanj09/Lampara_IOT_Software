import machine
import utime

# Configurar pines para filas y columnas (4 filas, 3 columnas)
filas = [machine.Pin(i, machine.Pin.OUT) for i in (16, 17, 18, 19)]
columnas = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in (20, 21, 22)]

# Definir matrices de sonidos para cada instrumento
guitarra = [
    ["Rasgueo 1", "Rasgueo 1", "Rasgueo 1"],
    ["Rasgueo 2", "Rasgueo 2", "Rasgueo 2"],
    ["Rasgueo 3", "Rasgueo 3", "Rasgueo 3"],
    ["0", "0", "0"]
]

tambor = [
    ["Tambor 1", "Tambor 1", "Tambor 1"],
    ["Tambor 2", "Tambor 2", "Tambor 2"],
    ["Tambor 3", "Tambor 3", "Tambor 3"],
    ["0", "0", "0"]
]

bateria = [
    ["Bombo", "Bombo", "Bombo"],
    ["Bombo", "Bombo", "Bombo"],
    ["Platillo", "Platillo", "Platillo"],
    ["0", "0", "0"]
]

caja_de_haija = [
    ["Golpe 1", "Golpe 1", "Golpe 1"],
    ["Golpe 2", "Golpe 2", "Golpe 2"],
    ["Golpe 3", "Golpe 3", "Golpe 3"],
    ["0", "0", "0"]
]

charango = [
    ["Rasgueo 1", "Rasgueo 1", "Rasgueo 1"],
    ["Rasgueo 2", "Rasgueo 2", "Rasgueo 2"],
    ["Rasgueo 3", "Rasgueo 3", "Rasgueo 3"],
    ["0", "0", "0"]
]

# Lista de nombres de instrumentos
nombres_instrumentos = ["Guitarra", "Tambor", "Batería", "c", "Charango"]

# Inicialmente usamos el instrumento guitarra
valores_matriz = guitarra
instrumentos = [guitarra, tambor, bateria, caja_de_haija, charango]
instrumento_actual = 0

estado_anterior = [[0 for _ in columnas] for _ in filas]

def matriz_estado():
    global valores_matriz, instrumento_actual
    instrumento_actual = (instrumento_actual + 1) % len(instrumentos)
    valores_matriz = instrumentos[instrumento_actual]
    print(f"Cambiado a {nombres_instrumentos[instrumento_actual]}")

def escanear_botones():
    estados = []
    for i, fila in enumerate(filas):
        fila.low()  # Activar la fila actual (baja)
        for j, columna in enumerate(columnas):
            if not columna.value():  # Si la columna está baja, el botón está presionado
                valor = valores_matriz[i][j]
                if valor == "0":
                    print(f"Botón de cambio presionado: ({i}, {j}), Valor: {valor}")
                    matriz_estado()
                else:
                    if estado_anterior[i][j] == 0:  # Si el estado anterior era 0, se acaba de presionar
                        print(f"Botón presionado: ({i}, {j}), Valor: {valor}")
                        estados.append((instrumento_actual, valor, 2))
                    estado_anterior[i][j] = 1  # Actualizar el estado a presionado
                while not columna.value():  # Esperar a que se libere el botón
                    utime.sleep_ms(10)
            else:
                if estado_anterior[i][j] == 1:  # Si el estado anterior era 1, se acaba de soltar
                    valor = valores_matriz[i][j]
                    estados.append((instrumento_actual, valor, 1))
                    print(f"Botón soltado: ({i}, {j}), Valor: {valor}")
                estado_anterior[i][j] = 0  # Actualizar el estado a no presionado
        fila.high()  # Desactivar la fila actual (alta)
    return estados

def obtener_estado_botones():
    return escanear_botones()
