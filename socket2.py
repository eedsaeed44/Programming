import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('w3shcools.com', 443))
cmd = 'GET https://www.w3schools.com/ HTTP\r\n\r\n'.encode()
mysock.send(cmd)
count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
    for n in data:
        count += 1
    with open('response.txt', 'a') as f:
        sys.stdout = f
        print(data.decode(),end='')
        sys.stdout = sys.__stdout__
# print(count)

mysock.close()