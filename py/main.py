import utime
from Wifi_lib import wifi_init
from teclado import escanear_botones, matriz_estado

def main():
    wifi_init()
    while True:
        escanear_botones()
        utime.sleep_ms(100)

if __name__ == "__main__":
    main()
