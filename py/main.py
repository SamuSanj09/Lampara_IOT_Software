from Wifi_lib import wifi_init
from teclado import escanear_botones, matriz_estado, valores_matriz, nombres_instrumentos, instrumentos, obtener_estado_botones
from database import send_data_to_database
import utime

def manejo_matriz(instrumento, sonido):
    print(f"Enviando datos del instrumento {instrumento} y sonido {sonido}")
    send_data_to_database(2, sonido, nombres_instrumentos[instrumento])
    utime.sleep(0.1)
    send_data_to_database(1, sonido, nombres_instrumentos[instrumento])

def main():
    wifi_init()
    while True:
        estados = obtener_estado_botones()
        for estado in estados:
            instrumento_actual, sonido, valor = estado
            manejo_matriz(instrumento_actual, sonido)
        utime.sleep_ms(100)

if __name__ == "__main__":
    main()
