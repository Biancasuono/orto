#https://miro.com/app/board/uXjVPhVQ7w0=/#
from fastapi import FastAPI   #fastapi libreria per comunicare tra programmi
from socket import socket # libreria per comunicazioni di rete in protocollo TCP=più sicuro ma più lento  (UDP dati volatili)
import time
import logging

app = FastAPI()  # oggetto contenente le funzioni della libreria

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

ecg_data_file=open("ecg_data_file.txt","a") # open dato preimpostato di pithon.il file sul quale si scrive (dati nuovi "a"= appende)

@app.get("/") # (@-un servizio) get, all'interno di fastapi. Solo un servizio di api attraverso il quale riceve dati da ESP (/). tra nome servio e parametri ce il punto di domanda ? es:("http://192.168.1.202:8000/?ecg_value=100")
async def save_send_to_sound(ecg_values:str,separator:str,delayms:int,board_name:str): # nome della funzione in utilizzo (def= definisco) ecg_value è lo stesso servizio dall'indirizzo sopra
    logger.info(ecg_values)
    logger.info("ciao")
    ecg_list=ecg_values.split(separator)
    for ecg_value in ecg_list:
        logger.info(ecg_value)
        ecg_data_file.write(str(ecg_value)+"\n") # scrivo nel file in un spazio di memoria, con il flush invia tutto nel file vero e proprio
        ecg_data_file.flush() # close oppure lo spzio esausto, allora invia i dati nel file, salvare nel disco fisico
        send_to_puredata(ecg_value) #nome della funzione (blu) (ecg_value)= il dato ricevuto riga,STRINGA 8. "questa funzione non esiste"
        time.sleep(delayms*0.001)
    send_to_puredata("0")
    return {"written":len(ecg_list)} # ti do indietro i dati ricchiesti dal client che sarebbe ESP

sock=socket()# spina_filo di collegamento
sock.connect(("127.0.0.1",3001))

def send_to_puredata(dato:str):
    dato=dato+";"
    sock.sendall(dato.encode('utf-8'))  #sendall (invia a socket)


print("per eseguire: uvicorn receiveECG:app --host 0.0.0.0 --port 8000 --reload")

# http://127.0.0.1:8000/?ecg_values=100I200I300I400I500&separator=I&delayms=100&board_name=ciao
