import socket
import mkdir
import upload
import json
import thread
import datetime
import download
import getFiles
import getDirs

class Server:
    def __init__(self):
        self.sock = socket.socket()
        self.host = "0.0.0.0"
        self.port = 5555
        self.username = "root"
        self.password = "root"
        self.cmds = {

                "upload":upload.upload,
                "mkdir":mkdir.mkdir,
                "getFiles":getFiles.getFiles,
                "download":download.download,
                "getDirs":getDirs.getDirs,

        }
    def run(self):
        print "PrivateBackup server is running."
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        while True:
            obj, conn = self.sock.accept()
            thread.start_new_thread(self.handle, (obj, conn[0]))


    def handle(self, obj, ip):
        data = ""
        while True:
            incoming = obj.recv(1024)
            if not incoming:
                break
            data += incoming
            if " EOT" in data:
                data = ' '.join(data.split()[:-1])
                break

        data = json.loads(data)
        print "{2} Incoming from {1} with data {0}".format(data, ip, datetime.datetime.now())
        if data['username'] == self.username and data['password'] == self.password:
            if data['cmd'] in self.cmds:
                self.cmds[data['cmd']](obj, data, ip)
            


if __name__ == "__main__":
    Server().run()


