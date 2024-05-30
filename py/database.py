import urequests
import ujson
from machine import RTC

def send_data_to_database(instrumento, valor, sonido, nombre_instrumento):
    url = "http://192.168.0.17/subida1.php"
    rtc = RTC()
    current_time = rtc.datetime()
    fecha_hora = f"{current_time[0]:04d}-{current_time[1]:02d}-{current_time[2]:02d} {current_time[4]:02d}:{current_time[5]:02d}:{current_time[6]:02d}"

    data = {
        'id1': instrumento,
        'valor': valor,
        'sonido': sonido,
        'HoraFecha': fecha_hora,
        'nombre_instrumento': nombre_instrumento
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
