from machine import Pin, ADC
import network
import urequests
import ujson
import time
from Wifi_lib import wifi_init

# Define los pines conectados a las filas y columnas
filas = [Pin(i, Pin.OUT) for i in (16, 17, 18, 19)]
columnas = [Pin(i, Pin.IN, Pin.PULL_UP) for i in (20, 21, 22)]

# Inicializar la conexión WiFi
wifi_init()

# Diccionario de instrumentos
instrumentos = {
    1: "guitarra",
    2: "bateria",
    3: "bajo",
    4: "tambor",
    5: "baquetas"
}

# Matriz de valores
valor_matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Función para manejar la matriz
def manejo_matriz(valor):
    for i in range(len(valor_matriz)):
        for j in range(len(valor_matriz[i])):
            valor_matriz[i][j] = valor
    for fila in valor_matriz:
        print(fila)

# Función para enviar datos a la base de datos
def send_data_to_database(instrumento, valor):
    url = "http://192.168.0.17/subida1.php"
    data = {
        'id1': instrumento,
        'valor': valor
    }
    print(f"Enviando información: {data}")
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = urequests.post(url, data=ujson.dumps(data), headers=headers)
        print(f"Respuesta del servidor: {response.text}")
    except OSError as e:
        print(f"Error al enviar datos: {e}")
    finally:
        if response:
            response.close()

# Función para leer el teclado matricial
def read_sensors():
    matriz_estado = [[0 for _ in columnas] for _ in filas]
    
    for i, fila in enumerate(filas):
        fila.value(1)
        time.sleep(0.01)

        for j, columna in enumerate(columnas):
            if columna.value() == 0:
                matriz_estado[i][j] = 1
            else:
                matriz_estado[i][j] = 0

        fila.value(0)
    
    return matriz_estado

# Función para identificar qué tecla fue presionada
def leer_teclado():
    matriz_estado = read_sensors()
    for i in range(len(matriz_estado)):
        for j in range(len(matriz_estado[i])):
            if matriz_estado[i][j] == 1:
                return (i, j)
    return None

def main():
    while True:
        # Leer valor del teclado matricial
        tecla_presionada = leer_teclado()
        if tecla_presionada:
            fila, columna = tecla_presionada
            valor = fila * len(columnas) + columna + 1
            if valor in instrumentos:
                manejo_matriz(valor)
                send_data_to_database(instrumentos[valor], valor)
            else:
                print("Tecla presionada no corresponde a un instrumento válido.")
        else:
            print("Introduce un valor: ")
            try:
                valor = int(input())
                manejo_matriz(valor)
                if valor in instrumentos:
                    send_data_to_database(instrumentos[valor], valor)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

if _name_ == "_main_":
    main()