import socket

host = "brounredo.no-ip.biz"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    buf = bytes(input(">>"), 'utf-8')
    s.send(buf)
    result = s.recv(1024)
    print(result)
    if buf == "exit":
        break
s.close()
