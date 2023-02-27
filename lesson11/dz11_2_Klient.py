import socket

HOST = '127.0.0.1'  # IP-адреса сервера
PORT = 65432        # Порт сервера

# Створення сокету
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter message to send to server: ")
        s.sendall(message.encode('utf-8'))  # Відправлення повідомлення серверу
        data = s.recv(1024)  # Отримання відповіді від сервера
        print(f"Received from server: {data.decode('utf-8')}")
