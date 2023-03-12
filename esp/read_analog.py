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
def loop(sleep_ms,send_count):
    adc = ADC(0)
    while True:
        pacco=""
        for i in range(send_count): #ciclo che ripete send_count il numero di vote il corpo che riceve
                                    # si ripete tutto qullo che sta dentro "for"
            r=adc.read()
            pacco=pacco+str(r)+"|"# r numero letto
            time.sleep(sleep_ms*0.001)

        try:
            urequests.get("http://192.168.1.202:8000/?ecg_values="+pacco+"&separator=I&delayms="+str(sleep_ms))
        except:
            pass
        print(r)
        time.sleep(sleep_seconds)

connect_wifi()
loop(100,100)
