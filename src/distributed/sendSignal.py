import signal
from time import sleep
import threading

def send_signals():
    while True:
        sleep(2)
        signal.pthread_kill(threading.main_thread().ident, signal.SIGUSR1)

sendSignal = threading.Thread(target=send_signals, args=())

def send_messages_to_central_server(signum, frame):
    print("send message to central server!")

signal.signal(signal.SIGUSR1, send_messages_to_central_server)
