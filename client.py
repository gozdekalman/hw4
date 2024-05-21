import socket
import threading

class ChatClient:
    def __init__(self, username, host='localhost', port=12345):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.username = username
        self.send_message(f'username:{username}')

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024)
                if message:
                    print(message.decode('utf-8'))
            except:
                print('An error occurred.')
                self.client.close()
                break

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))

    def run(self):
        threading.Thread(target=self.receive_messages).start()
        while True:
            message = input('')
            self.send_message(message)
