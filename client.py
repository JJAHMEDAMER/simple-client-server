import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Make Socket
soc.connect(('www.dj4e.com', 80))  # Make Connection

cmd = 'GET https://www.dj4e.com/ \r\n\r\n'.encode()  # Request and encode to sent in utf8 python use unicode
soc.send(cmd)  # Send request

while True:
    data = soc.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

soc.close()