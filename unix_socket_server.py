import socket
import os

class UnixSocketServer:
    def __init__(self, socket_path="/tmp/unix_socket_server.sock"):
        self.socket_path = socket_path
        self.server_socket = None

    def start(self):
        if os.path.exists(self.socket_path):
            os.remove(self.socket_path)

        self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.server_socket.bind(self.socket_path)
        self.server_socket.listen(1)

    def receive_command(self):
        connection, _ = self.server_socket.accept()
        command = connection.recv(1024).decode("utf-8")
        connection.close()
        return command.strip()

    def stop(self):
        self.server_socket.close()
        os.remove(self.socket_path)
