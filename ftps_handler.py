from ftplib import FTP_TLS

class FTPSHandler:
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
        ftps = FTP_TLS()
        ftps.connect(self.command["address"], int(self.command["portnumber"]))
        ftps.login(self.command["user"], self.command["passwd"])
        ftps.prot_p()

        with open(self.command["file"], "rb") as f:
            ftps.storbinary(f"STOR {self.command['to']}", f)

        ftps.quit()

    def pull(self):
        ftps = FTP_TLS()
        ftps.connect(self.command["address"], int(self.command["portnumber"]))
        ftps.login(self.command["user"], self.command["passwd"])
        ftps.prot_p()

        with open(self.command["to"], "wb") as f:
            ftps.retrbinary(f"RETR {self.command['file']}", f.write)

        ftps.quit()
