from wifi_lib import wifi_init
from database import send_data_to_database
from machine import RTC

def main():
    # Inicializar la conexión WiFi
    wifi_init()
    
    # Datos de prueba
    instrumento = 1
    valor = 100
    sonido = "Acorde G"
    nombre_instrumento = "Guitarra"
    
    # Enviar datos de prueba a la base de datos
    send_data_to_database(instrumento, valor, sonido, nombre_instrumento)

if __name__ == "__main__":
    main()
