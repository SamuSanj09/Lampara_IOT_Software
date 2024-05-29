import machine
import utime

# Configurar pines para filas y columnas (4 filas, 3 columnas)
filas = [machine.Pin(i, machine.Pin.OUT) for i in (16, 17, 18, 19)]
columnas = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in (20, 21, 22)]

def read_sensors():
    matriz_estado = [[0 for _ in columnas] for _ in filas]
    
    for i, fila in enumerate(filas):
        fila.value(1)
        utime.sleep(0.01)

        for j, columna in enumerate(columnas):
            if columna.value() == 0:
                matriz_estado[i][j] = 1
            else:
                matriz_estado[i][j] = 0

        fila.value(0)
    
    return matriz_estado

def leer_teclado():
    matriz_estado = read_sensors()
    for i in range(len(matriz_estado)):
        for j in range(len(matriz_estado[i])):
            if matriz_estado[i][j] == 1:
                return (i, j)
    return None

def escanear_botones(callback):
    for i, fila in enumerate(filas):
        fila.low()  # Activar la fila actual (baja)
        for j, columna in enumerate(columnas):
            if not columna.value():  # Si la columna está baja, el botón está presionado
                callback(i, j)
                while not columna.value():  # Esperar a que se libere el botón
                    utime.sleep_ms(10)
        fila.high()  # Desactivar la fila actual (alta)
