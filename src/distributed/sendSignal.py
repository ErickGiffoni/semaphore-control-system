import signal
from time import sleep
from threading import Thread

def send_signals():
    while True:
        sleep(2)
        signal.raise_signal(signal.SIGUSR1)

sendSignal = Thread(target=send_signals, args=())

def send_messages_to_central_server(signum, frame):
    print("send message to central server!")

signal.signal(signal.SIGUSR1, send_messages_to_central_server)
