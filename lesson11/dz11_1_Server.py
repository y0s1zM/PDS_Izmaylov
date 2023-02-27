import socket

HOST = '127.0.0.1'  # IP-адреса сервера
PORT = 65432        # Порт сервера

# Створення сокету
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()  # Очікування з'єднання з клієнтом
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)  # Отримання даних від клієнта
            if not data:
                break
            print(f"Received from client: {data.decode('utf-8')}")
            message = input("Enter message to send to client: ")
            conn.sendall(message.encode('utf-8'))  # Відправлення відповіді клієнту