import socket
import threading
from user_manager import UserManager

class ChatServer:
    def __init__(self, host='localhost', port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(5)
        self.clients = []
        self.user_manager = UserManager()

    def broadcast(self, message, client):
        for c in self.clients:
            if c != client:
                try:
                    c.send(message.encode('utf-8'))
                except:
                    self.clients.remove(c)

    def handle_client(self, client):
        client_username = None
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message.startswith('username:'):
                    client_username = message.split(':')[1]
                    self.user_manager.add_user(client_username)
                    welcome_message = f"User {client_username} joined the chat."
                    self.user_manager.get_user(client_username).add_message(welcome_message)
                    self.broadcast(welcome_message, client)
                else:
                    if client_username:
                        user = self.user_manager.get_user(client_username)
                        user.add_message(message)
                        formatted_message = f"{client_username}: {message}"
                        self.broadcast(formatted_message, client)
            except:
                if client_username:
                    self.clients.remove(client)
                    self.broadcast(f"User {client_username} left the chat.", client)
                    client.close()
                break

    def run(self):
        print('Server is running...')
        while True:
            client, addr = self.server.accept()
            print(f'Connected by {addr}')
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client,)).start()
