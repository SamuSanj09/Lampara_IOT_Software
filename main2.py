from machine import Pin, ADC
import network
import urequests
import ujson
import time
from Wifi_lib import wifi_init

# Definición de pines y estados iniciales
led = Pin('LED', Pin.OUT)
btn = Pin(18, Pin.IN, Pin.PULL_UP)

ledR = Pin(6, Pin.OUT)
ledG = Pin(7, Pin.OUT)
ledB = Pin(8, Pin.OUT)
adc = ADC(Pin(26))  # Pin del LM35
setpoint_adc = ADC(Pin(27))  # Pin del ADC del setpoint

# Inicializar la conexión WiFi
wifi_init()

# Arreglo para instrumentos
instrumentos = {
    1: "guitarra",
    2: "bateria",
    3: "bajo",
    4: "tambor",
    5: "baquetas"
}

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

def main():
    while True:
        for i in sorted(instrumentos.keys()):
            print(f"\n{i}. {instrumentos[i]}")
        # Obtener la selección del usuario
        seleccion = int(input("Ingrese el número del instrumento: "))
        
        # Verificar si la selección es válida
        if seleccion in instrumentos:
            # Asignar el valor correspondiente al instrumento seleccionado
            valor = seleccion
            # Obtener el ID aleatorio (simulado)
            id1 = 2  # Simulando un ID aleatorio
            # Enviar los datos a la base de datos
            send_data_to_database(instrumentos[seleccion], valor)
        else:
            print("Selección inválida")
        
        # Esperar un tiempo antes de enviar los siguientes datos
        time.sleep(2)  # Esperar 10 segundos

if __name__ == "__main__":
    main()
