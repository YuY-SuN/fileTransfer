import paramiko

class SFTPHandler:
    def __init__(self, command):
        self.command = command

    def execute(self):
        if self.command["action"] == "put":
            self.put()
        elif self.command["action"] == "pull":
            self.pull()
        else:
            print(f"Unknown action: {self.command['action']}")

    def put(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.command["address"], int(self.command["portnumber"]), key_filename=self.command["pkey"])

        sftp = ssh.open_sftp()
        sftp.put(self.command["file"], self.command["to"])
        sftp.close()

        ssh.close()

    def pull(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.command["address"], int(self.command["portnumber"]), key_filename=self.command["pkey"])

        sftp = ssh.open_sftp()
        sftp.get(self.command["file"], self.command["to"])
        sftp.close()

        ssh.close()
