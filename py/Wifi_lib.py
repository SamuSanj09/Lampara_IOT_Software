import rp2
import network
import ubinascii
import urequests as requests
from secrets import secrets
import socket
from machine import Pin
import time
import utime
import gc

def wifi_init():
    # Set country to avoid possible errors  
    rp2.country('DE')

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) 
    # If you need to disable powersaving mode
    # wlan.config(pm = 0xa11140)

    # See the MAC address in the wireless chip OTP
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print('mac = ' + mac)

    # Other things to query
    print('Canal = ' + str(wlan.config('channel')))
    print('SSID = ' + wlan.config('ssid'))
    print('RSSI = ' + str(wlan.config('txpower')))

    # Load login data from different file for safety reasons
    ssid = secrets['ssid']
    pw = secrets['pw']

    wlan.connect(ssid, pw)

    # Wait for connection with 10 second timeout
    timeout = 10
    while timeout > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        timeout -= 1
        print('Waiting for connection...')
        time.sleep(1)
        
    # Handle connection error
    # Error meanings
    # 0  Link Down
    # 1  Link Join
    # 2  Link NoIp
    # 3  Link Up
    # -1 Link Fail
    # -2 Link NoNet
    # -3 Link BadAuth
    if wlan.status() != 3:
        raise RuntimeError('Wi-Fi connection failed')
    else:
        """      
        for i in range(wlan.status()):
            intled.on()
            time.sleep(0.2)
            intled.off()
            time.sleep(0.2)
        """
        print('Connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
        
        
# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()        
    return html

