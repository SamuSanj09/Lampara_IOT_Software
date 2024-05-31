import urequests
import ujson

def send_data_to_database(valor, sonido, nombre_instrumento):
    url = "http://192.168.43.216/Lampara_IOT/php/subida.php"
    # Cambia esta URL según sea necesario

    data = {
        'valor': valor,
        'sonido': sonido,
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

