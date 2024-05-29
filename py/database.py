import urequests
import ujson
from datetime import datetime

def send_data_to_database(instrumento, valor, sonido, nombre_instrumento):
    url = "http://192.168.0.17/subida.php"
    data = {
        'id1': instrumento,
        'valor': valor,
        'sonido': sonido,
        'HoraFecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
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
