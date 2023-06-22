import sys
import threading
from unix_socket_server import UnixSocketServer
from command_parser import parse_command
from ftps_handler import FTPSHandler
from sftp_handler import SFTPHandler

def main():
    server = UnixSocketServer()
    server.start()

    while True:
        command = server.receive_command()
        if command == "exit":
            break

        parsed_command = parse_command(command)
        if parsed_command["protocol"] == "ftps":
            handler = FTPSHandler(parsed_command)
        elif parsed_command["protocol"] == "sftp":
            handler = SFTPHandler(parsed_command)
        else:
            print(f"Unknown protocol: {parsed_command['protocol']}")
            continue

        action_thread = threading.Thread(target=handler.execute)
        action_thread.start()

    server.stop()
    sys.exit(0)

if __name__ == "__main__":
    main()
