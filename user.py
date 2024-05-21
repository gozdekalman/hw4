import json

class User:
    def __init__(self, username):
        self.username = username
        self.messages = []
        self.load_messages()

    def add_message(self, message):
        self.messages.append(message)
        self.save_messages()

    def get_messages(self):
        return self.messages

    def search_messages(self, keyword):
        return [message for message in self.messages if keyword in message]

    def save_messages(self):
        with open(f'{self.username}_messages.json', 'w') as f:
            json.dump(self.messages, f)

    def load_messages(self):
        try:
            with open(f'{self.username}_messages.json', 'r') as f:
                self.messages = json.load(f)
        except FileNotFoundError:
            self.messages = []

    def __str__(self):
        return self.username
