from Wifi_lib import wifi_init
from teclado import escanear_botones, matriz_estado, valores_matriz, nombres_instrumentos, instrumentos, obtener_estado_botones
from database import send_data_to_database
import utime

def manejo_matriz(instrumento, sonido, valor):
    print(f"Enviando datos del instrumento {instrumento} y sonido {sonido}, valor {valor}")
    send_data_to_database(valor, sonido, nombres_instrumentos[instrumento])

def main():
    wifi_init()
    while True:
        estados = obtener_estado_botones()
        for estado in estados:
            instrumento_actual, sonido, valor = estado
            manejo_matriz(instrumento_actual, sonido, valor)
        utime.sleep_ms(100)

if __name__ == "__main__":
    main()
