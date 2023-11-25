import socket

class Server:
    def connect(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(1)
        self.client, self.addr = self.server.accept()

    def receive(self):
        response = None
        while not response:
            response = self.client.recv(1024).decode()
        return response

    def send(self, message):
        self.client.send(message.encode())

    def close(self):
        self.client.close()
        self.server.close()
