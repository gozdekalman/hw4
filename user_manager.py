from user import User

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)

    def get_user(self, username):
        return self.users.get(username)

    def group_users(self):
        groups = {"friends": [], "family": [], "others": []}
        for username, user in self.users.items():
            # Here you can define your own grouping logic
            if username.startswith('friend_'):
                groups['friends'].append(user)
            elif username.startswith('family_'):
                groups['family'].append(user)
            else:
                groups['others'].append(user)
        return groups

    def search_messages(self, keyword):
        result = {}
        for username, user in self.users.items():
            result[username] = user.search_messages(keyword)
        return result
