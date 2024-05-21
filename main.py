from server import ChatServer
from client import ChatClient

def main():
    choice = input("Server (s) or Client (c)? ")
    if choice == 's':
        server = ChatServer()
        server.run()
    elif choice == 'c':
        username = input("Enter your username: ")
        client = ChatClient(username)
        client.run()

if __name__ == "__main__":
    main()
