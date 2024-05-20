import os
import socket
import sys
import threading


def send_message(s):
    while True:
        try:
            message_out = input()
            s.send(message_out.encode("ASCII"))
        except (EOFError):
            break

def receive_message(s):
    while True:
        try:
            message_in = s.recv(1024).decode("ASCII")
            if message_in:
                print(message_in)
            else:
                break
        except (EOFError, socket.error, ConnectionResetError):
            break

def client(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    send_thread = threading.Thread(target=send_message, args=(s,), daemon=True)
    receive_thread = threading.Thread(target=receive_message, args=(s,), daemon=True)

    send_thread.start()
    receive_thread.start()
    
    while send_thread.is_alive() and receive_thread.is_alive():
        pass
    receive_thread.join(0.4)
    send_thread.join(0.3)
    
    s.close()
    sys.exit(0)
    

port = int(sys.argv[1])
client(port, "localhost")
