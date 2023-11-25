import socket

class Client:
    def connect(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send(self, message):
        self.client.send(message.encode())

    def receive(self):
        response = None
        while not response:
            response = self.client.recv(1024).decode()
        return response

    def close(self):
        self.client.close()
