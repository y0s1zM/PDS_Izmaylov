import socket
import re

HOST = '127.0.0.1'  # IP-адреса сервера
PORT = 65432  # Порт сервера

# Створення словника з запитами та відповідями чат-бота
bot_responses = {
    r'.*(Привіт|Вітаю|Здоровенькі були).*': 'Привіт, як справи?',
    r'.*(Як справи|Що нового|Як життя).*': 'Все добре, дякую!',
    r'.*(Погода|Яка погода).*': 'Зараз на вулиці гарна погода!'
}


# Створення функції для відповіді клієнту за допомогою чат-бота
def bot_response(message):
    for pattern, response in bot_responses.items():
        if re.match(pattern, message):
            return response
    return "Не розумію, що ви маєте на увазі."


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
            message = data.decode('utf-8')
            print(f"Received from client: {message}")

            # Виклик функції для відповіді клієнту за допомогою чат-бота
            bot_reply = bot_response(message)
            print(f"Bot reply: {bot_reply}")
            conn.sendall(bot_reply.encode('utf-8'))  # Відправлення відповіді клієнту

