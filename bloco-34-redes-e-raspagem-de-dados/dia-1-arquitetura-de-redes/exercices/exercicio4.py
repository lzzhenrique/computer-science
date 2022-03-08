from socketserver import BaseRequestHandler, TCPServer


class TCPHandler(BaseRequestHandler):

    def handle(self):
        connect_msg = 'Ola, client!!\n'
        self.request.sendall(connect_msg.encode())
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.request.sendall(self.data + '\n'.encode())


if __name__ == "__main__":
    HOST, PORT = "localhost", 8098

    with TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()
