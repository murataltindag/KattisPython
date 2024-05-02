import socket
import sys


def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(('', port))

    s.listen(5)

    c, addr = s.accept()

    while(True):
        message = c.recv(1024).decode("ASCII")
        if not message:
            break
        print(message[::-1])

    c.close()

def client(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #port = port

    s.connect((host, port))
    
    while(True):
        try:
            message = input()
            s.send(message.encode("ASCII"))
        except EOFError:
            break
    
    s.close()

if len(sys.argv) != 3:
    print("Usage as server: python messenger.py -s <port number>")
    print("Usage as client: python messenger.py <port number> <server host name>")
    sys.exit(1)

is_server = False

if sys.argv[1] == "-s":
    is_server = True
    port = int(sys.argv[2])
else:
    port = int(sys.argv[1])
    host = sys.argv[2]
    
if is_server:
    server(port)
else:
    client(port, host)

