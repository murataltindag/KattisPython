import socket
import sys
import threading

clients = []

def handle_client(c):
    try:
        username = c.recv(1024).decode("ASCII")
        while True:
            message = username + ": " + c.recv(1024).decode("ASCII")
            if not message:
                break
            for client in clients:
                if client != c:
                    client.send(message.encode("ASCII"))
    except ConnectionResetError:
        pass
    finally:
        c.close()
        clients.remove(c)

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        clients.append(c)
        client_thread = threading.Thread(target=handle_client, args=(c,))
        client_thread.start()


port = int(sys.argv[1])
server(port)