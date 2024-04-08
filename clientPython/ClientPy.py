import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.30.114.36', 8888))




while True:
    data = client.recv(1024).decode()
    print(data)

    if "The game is starting" in data:
        break
turn_count=0
while True:
    turn_count+=1
    data = client.recv(1024).decode()
    print(data)

    if "Your turn" in data:
        position = input("Enter your move (0-8): ")
        client.send(position.encode())
        print(client.recv(1024).decode())

    if "wins!" in data or "draw" in data:
        break
    if turn_count>10:
        break

client.close()