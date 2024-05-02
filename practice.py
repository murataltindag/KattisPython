import socket
import sys


def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.bind(('', port))
    
    s.listen(5)
    
    c, addr = s.accept()