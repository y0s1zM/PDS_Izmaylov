
import socket
import logging

HOST = ''
PORT = 8888

logger = logging.getLogger('chat_server')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('chat_server.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
logger.info('Connected by %s', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    logger.info('Message received: %s', data)

conn.close()
logger.info('Connection closed')

