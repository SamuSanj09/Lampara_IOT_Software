import machine
import utime

# Configurar pines individuales para botones
botones_pines = [27, 26, 25, 24]
botones = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for pin in botones_pines]

def escanear_botones():
    for i, boton in enumerate(botones):
        if not boton.value():  # Si el botón está presionado (valor es 0)
            print(f"Botón {i+1} (Pin {botones_pines[i]}) presionado")
            while not boton.value():  # Esperar a que se libere el botón
                utime.sleep_ms(10)

def main():
    print("Iniciando prueba de botones...")
    while True:
        escanear_botones()
        utime.sleep_ms(100)

if __name__ == "__main__":
    main()
