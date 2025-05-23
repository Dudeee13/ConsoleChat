import socket
import threading
client_message = str()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_name = input("Введіть своє ім'я ")
client_socket.connect(("localhost", 8080))
client_socket.send(user_name.encode())
def send_message():
    while True:
        client_message = input()
        if client_message.lower() == "exit":
            client_socket.close()
            break
        client_socket.send(client_message.encode())
threading.Thread(target=send_message).start()
while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
    except:
        break