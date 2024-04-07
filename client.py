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


def string_to_binary(string):
    binary_result = ''.join(format(ord(char), '08b') for char in string)
    return binary_result


def send_tcp_requests(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    for bit in message:
        if bit == '0':
            time.sleep(ZERO_DELAY)
            client_socket.sendall(b'TCP Request')
        else:
            time.sleep(ONE_DELAY)
            client_socket.sendall(b'TCP Request')

    time.sleep(CLOSE_DELAY)
    client_socket.sendall(b'TCP Request')
    client_socket.close()


message = input("Enter your message: ")
message = string_to_binary(message)
send_tcp_requests(message)
