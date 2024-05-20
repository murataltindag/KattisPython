import socket
import sys
import threading


def send_message(s, host, file_port):
    while True:
        try:
            command = input("Enter an option ('m', 'f', 'x'): \n \
                        (M)essage (send) \n \
                        (F)ile (request) \n \
                        e(X)it) \n").lower()
            if command == 'm':
                message_out = input("Enter your message: \n")
                s.send(message_out.encode("ASCII"))
            elif command == 'f':
                filename = input("Which file do you want?\n")
                file_request(host, file_port, filename)
            elif command == 'x':
                print("closing your sockets...goodbye")
                s.shutdown(socket.SHUT_WR)
                s.close()
                break
            else:
                print("Invalid option")
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

def server_listen(s):
    try:
        while True:
            c, addr = s.accept()
            filename = c.recv(1024).decode("ASCII")
            try:
                with open(filename, 'rb') as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        c.sendall(data)
                print(f"File '{filename}' sent successfully")
            except FileNotFoundError:
                print(f"File '{filename}' not found")
            c.close()
    except (EOFError, socket.error, ConnectionResetError):
        pass
        
def client_listen(file_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', file_port))
        s.listen(5)
        while True:
            c, addr = s.accept()
            filename = c.recv(1024).decode("ASCII")
            try:
                with open(filename, 'rb') as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        c.sendall(data)
                print(f"File '{filename}' sent successfully")
            except FileNotFoundError:
                print(f"File '{filename}' not found")
            c.close()
    except (EOFError, socket.error, ConnectionResetError):
        pass

def file_request(host, port, filename):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(filename.encode("ASCII"))
    print(f"File '{filename}' ready to be received")
    with open('received_' + filename, 'wb') as file:
        while True:
            data = s.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"File '{filename}' received successfully")
    s.close()

# SERVER

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print(f"Server listening on port {port}")
    c, addr = s.accept()
    print(f"Connected by {addr}")
    
    file_port = c.recv(1024).decode("ASCII")
    file_port = int(file_port)

    send_thread = threading.Thread(target=send_message, args=(c, 'localhost', file_port,), daemon=True)
    receive_thread = threading.Thread(target=receive_message, args=(c,), daemon=True)
    listen_thread = threading.Thread(target=server_listen, args=(s,), daemon=True)

    send_thread.start()
    receive_thread.start()
    listen_thread.start()
    
    
    while send_thread.is_alive() and receive_thread.is_alive():
        pass
    receive_thread.join(0.4)
    send_thread.join(0.3)
    listen_thread.join(0.3)

    # c.shutdown(socket.SHUT_WR)
    c.close()

# CLIENT 

def client(port, host, file_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f"Connected to server at {host}:{port}")
    s.send(file_port.encode("ASCII"))
    file_port = int(file_port)

    send_thread = threading.Thread(target=send_message, args=(s, host, file_port,), daemon=True)
    receive_thread = threading.Thread(target=receive_message, args=(s,), daemon=True)
    listen_thread = threading.Thread(target=client_listen, args=(file_port,), daemon=True)

    send_thread.start()
    receive_thread.start()
    listen_thread.start()
    
    while send_thread.is_alive() and receive_thread.is_alive():
        pass
    receive_thread.join(0.4)
    send_thread.join(0.3)
    listen_thread.join(0.3)

    s.shutdown(socket.SHUT_WR)
    s.close()

# MAIN   

if len(sys.argv) not in [3, 5, 7]:
    print("Usage as server: python messenger_with_files.py -l <listening port number> ")
    print("Usage as client: python messenger_with_files.py -l <listening port number> \
        -p <connect server port> [-s] [connect server address] ")
    sys.exit(1)

is_server = False
port = int(sys.argv[2])

if len(sys.argv) == 3:
    is_server = True
else:
    file_port = sys.argv[2]
    port = int(sys.argv[4])
    if len(sys.argv) == 7:
        host = sys.argv[6]
    else:
        host = 'localhost'
    
if is_server:
    server(port)
else:
    client(port, host, file_port)
