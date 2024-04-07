import socket
import time
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_IP = os.getenv("SERVER_IP_ADDRESS")
SERVER_PORT = int(os.getenv("SERVER_PORT"))


ZERO_DELAY = float(os.getenv("ZERO_BIT_DELAY"))
ONE_DELAY = float(os.getenv("ONE_BIT_DELAY"))
CLOSE_DELAY = float(os.getenv("CLOSE_SOCKET_DELAY"))


def binary_to_string(binary):
    string_result = ''.join(chr(int(binary[i:i+8], 2))
                            for i in range(0, len(binary), 8))
    return string_result


def process_tcp_request(server_socket):
    msg = ''
    while True:

        start = time.time()
        data = server_socket.recv(1024)
        end = time.time()

        if not data:
            break

        if end - start > CLOSE_DELAY:
            print(binary_to_string(msg))
            break
        elif end - start > ONE_DELAY:
            msg += '1'

        else:
            msg += '0'

    server_socket.close()


welcoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcoming_socket.bind((SERVER_IP, SERVER_PORT))
welcoming_socket.listen(1)

print("Server listening on port 3000...")

while True:
    server_socket, addr = welcoming_socket.accept()
    process_tcp_request(server_socket)
0
