
class User:
    def __init__(self, username):
        self.username = username
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def search_messages(self, keyword):
        return [message for message in self.messages if keyword in message]

    def __str__(self):
        return self.username
