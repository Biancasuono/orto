from machine import ADC
import time
import urequests
from config import *

board_name="esp1"

def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to wifi")
        wlan.connect(wifi_name,wifi_pass)
        while not wlan.isconnected(): #attenzione al not
            pass # comando vuoto
    print("connected")

# per interrompere ctrl-c
def loop(sleep_ms,send_count):
    adc = ADC(0)
    while True:
        pacco=""
        for i in range(send_count): #ciclo che ripete send_count il numero di vote il corpo che riceve
                                    # si ripete tutto qullo che sta dentro "for"
            r=adc.read()
            pacco=pacco+str(r)+"I"# r numero letto
            time.sleep(sleep_ms*0.001)

        try:
            urequests.get(url_receiver+"/?ecg_values="+pacco+"&separator=I&delayms="+str(sleep_ms)+"&board_name="+board_name)
        except:
            pass
        print(r)

connect_wifi()
loop(loop_time_ms,impulses_per_pack)
