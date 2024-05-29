import utime
from wifi import initialize_wifi
from database import send_data_to_database
from keyboard import leer_teclado, escanear_botones
import instruments

# Inicializar la conexión WiFi
initialize_wifi()

# Diccionario de instrumentos para la base de datos
instrumentos_db = {
    1: "guitarra",
    2: "bateria",
    3: "bajo",
    4: "tambor",
    5: "baquetas"
}

def main():
    while True:
        # Leer valor del teclado matricial
        tecla_presionada = leer_teclado()
        if tecla_presionada:
            fila, columna = tecla_presionada
            valor = fila * 3 + columna + 1  # Asumiendo que hay 3 columnas
            if valor in instrumentos_db:
                instruments.manejo_matriz(valor, instruments.valores_matriz)
                sonido = instruments.valores_matriz[fila][columna]
                nombre_instrumento = instruments.nombres_instrumentos[instruments.instrumento_actual]
                send_data_to_database(instrumentos_db[valor], valor, sonido, nombre_instrumento)
            else:
                print("Tecla presionada no corresponde a un instrumento válido.")
        else:
            print("Introduce un valor: ")
            try:
                valor = int(input())
                instruments.manejo_matriz(valor, instruments.valores_matriz)
                if valor in instrumentos_db:
                    sonido = "Manual"
                    nombre_instrumento = "Manual"
                    send_data_to_database(instrumentos_db[valor], valor, sonido, nombre_instrumento)
            except ValueError:
                print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    while True:
        escanear_botones(lambda i, j: instruments.cambiar_instrumento() if instruments.valores_matriz[i][j] == "0" else print(f"Botón presionado: ({i}, {j}), Valor: {instruments.valores_matriz[i][j]}"))
        utime.sleep_ms(100)
