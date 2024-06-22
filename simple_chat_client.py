# simple_chat_client.py
import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("You: ")
        client_socket.sendall(message.encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client('127.0.0.1', 65432)
