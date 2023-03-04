#https://miro.com/app/board/uXjVPhVQ7w0=/#
from fastapi import FastAPI   #fastapi libreria per comunicare tra programmi
from socket import socket # libreria per comunicazioni di rete in protocollo TCP=più sicuro ma più lento  (UDP dati volatili)

app = FastAPI()  # oggetto contenente le funzioni della libreria

ecg_data_file=open("ecg_data_file.txt","a") # open dato preimpostato di pithon.il file sul quale si scrive (dati nuovi "a"= appende)

@app.get("/") # (@-un servizio) get, all'interno di fastapi. Solo un servizio di api attraverso il quale riceve dati da ESP (/). tra nome servio e parametri ce il punto di domanda ? es:("http://192.168.1.202:8000/?ecg_value=100")
async def save_send_to_sound(ecg_value:str): # nome della funzione in utilizzo (def= definisco) ecg_value è lo stesso servizio dall'indirizzo sopra
    ecg_data_file.write(str(ecg_value)+"\n") # scrivo nel file in un spazio di memoria, con il flush invia tutto nel file vero e proprio
    ecg_data_file.flush() # close oppure lo spzio esausto, allora invia i dati nel file, salvare nel disco fisico
    send_to_puredata(ecg_value) #nome della funzione (blu) (ecg_value)= il dato ricevuto riga,STRINGA 8. "questa funzione non esiste"
    return {"written":ecg_value} # ti do indietro i dati ricchiesti dal client che sarebbe ESP

sock=socket()# calza di collegamento
sock.connect(("127.0.0.1",3001))

def send_to_puredata(dato:str):
    dato=dato+";"
    sock.sendall(dato.encode('utf-8'))  #sendall (invia a socket)
