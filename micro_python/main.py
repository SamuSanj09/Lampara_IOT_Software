from machine import Pin, ADC
import network
import urequests
import ujson
import random
import time
from Wifi_lib import wifi_init

# Definición de pines y estados iniciales
led = Pin('LED', Pin.OUT)
btn = Pin(18, Pin.IN, Pin.PULL_UP)

ledR = Pin(6, Pin.OUT)
ledG = Pin(7, Pin.OUT)
ledB = Pin(8, Pin.OUT)
relay = Pin(10, Pin.OUT)  # Relé controlado por el botón
pinadc = 26  # Pin del LM35
pinsetpoint = 27  # Pin del ADC del setpoint

wifi_init()

# Estado inicial del relé y LEDs
relay_state = False  # False indica que el relé está apagado
relay.value(relay_state)

def send_data_to_database(lamp_id, usuario, temp_value, temp_int, sep_point, lamp_on_off):
    url = "http://192.168.43.216/Lampara_IOT/php/save_data.php"
    data = {
        'UserID': usuario,
        'LampID': lamp_id,
        'temp_value': temp_value,
        'temp_int': temp_int,
        'sep_point': sep_point,
        'LampOnOff': lamp_on_off
    }
    print(f"Informacion: {data}")
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = urequests.post(url, data=ujson.dumps(data), headers=headers)
        print(f"Server response: {response.text}")
    except OSError as e:
        print(f"Failed to send data: {e}")
    finally:
        if response:
            response.close()

def read_sensors():
    # Simulando lectura de sensores
    temp_value = random.uniform(20.0, 30.0)
    temp_int = random.randint(20, 30)
    sep_point = random.randint(50, 60)
    return temp_value, temp_int, sep_point

def toggle_relay():
    global relay_state
    relay_state = not relay_state  # Cambiar el estado del relé
    relay.value(relay_state)
    ledR.value(relay_state)
    ledG.value(relay_state)
    ledB.value(relay_state)
    print(f"Relay state changed to: {relay_state}")

def get_last_lamp_state(lamp_id):
    url = f"http://192.168.43.216/Lampara_IOT/php/ultimo_estado.php?LampID={lamp_id}&UserID=1&obtener_estado=true"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            data = ujson.loads(response.text)
            print(f"Last lamp state: {data}")
            if data['success']:
                return data['currentState']
            else:
                print(f"Error: {data['error']}")
                return None
        else:
            print(f"Failed to get last lamp state: {response.status_code}")
            return None
    except OSError as e:
        print(f"Failed to get last lamp state: {e}")
        return None
    finally:
        if response:
            response.close()

def update_relay_state():
    global relay_state
    last_state = get_last_lamp_state("Lamp01")
    if last_state is not None:
        relay_state = (last_state == 2)
        relay.value(relay_state)
        ledR.value(relay_state)
        ledG.value(relay_state)
        ledB.value(relay_state)
        print(f"Updated relay state to: {relay_state}")

previous_value = btn.value()

# Bucle principal
while True:
    # Verificar el estado del botón
    current_value = btn.value()
    if previous_value == 1 and current_value == 0:
        # El botón fue presionado
        toggle_relay()
        lamp_on_off = 2 if relay_state else 1
        temp_value, temp_int, sep_point = read_sensors()
        send_data_to_database("Lamp01", 1, temp_value, temp_int, sep_point, lamp_on_off)
        
    previous_value = current_value
    
    # Actualizar el estado del relé cada 2 segundos
    update_relay_state()
    time.sleep(2)

