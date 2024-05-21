import socket
import threading
import json

class ChatClient:
    def __init__(self, username, host='localhost', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.username = username
        self.send_message(f'username:{username}')

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                try:
                    data = json.loads(message)
                    if isinstance(data, list):
                        print("Past messages:")
                        for msg in data:
                            print(msg)
                    elif isinstance(data, dict):
                        if 'friends' in data and 'family' in data and 'others' in data:
                            print("User groups:")
                            for group, users in data.items():
                                print(f"{group.capitalize()}:")
                                for user in users:
                                    print(f"  {user}")
                        else:
                            print("Search results:")
                            for user, messages in data.items():
                                print(f"{user}:")
                                for msg in messages:
                                    print(f"  {msg}")
                except json.JSONDecodeError:
                    print(message)
            except Exception as e:
                print('An error occurred:', e)
                self.client.close()
                break

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

    def run(self):
        threading.Thread(target=self.receive_messages).start()
        while True:
            message = input('')
            self.send_message(message)
