from machine import ADC
import time
import urequests

def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to wifi")
        wlan.connect("WebPocket-3C49","B1KZNKAQ")
        while not wlan.isconnected(): #attenzione al not
            pass # comando vuoto
    print("connected")

# per interrompere ctrl-c
def loop(sleep_seconds=0.1):
    adc = ADC(0)
    while True:
        r=adc.read()
        try:
            urequests.get("http://192.168.1.202:8000/?ecg_value="+str(r))
        except:
            pass
        print(r)
        time.sleep(sleep_seconds)

connect_wifi()
loop()
