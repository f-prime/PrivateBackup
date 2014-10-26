import json
import thread
import socket
import upload
import mkdir
import os
import time
import datetime
import download

class Client:
    def __init__(self):
        self.host = ""
        self.port = 5555
        self.dirs = []
        self.files = {}
        self.username = "root"
        self.password = "root"
        self.usercmds = {"download":download.download}

    def run(self):  
        thread.start_new_thread(self.shell, ())
        while True:
            self.scandirs()
            self.scanfiles()
            time.sleep(5)


    def scandirs(self):
        for x,y,z in os.walk("files"):
            if x not in self.dirs:
                self.dirs.append(x)
                try:
                    sock = socket.socket()
                    sock.connect((self.host, self.port))
                    mkdir.mkdir(sock, x, self.username, self.password)
                    print "{0} Outgoing mkdir {1}".format(datetime.datetime.now(), x)
                except Exception, e:
                    self.dirs.remove(x) # Remove it so that it is tried again later
                time.sleep(0.5)


        for x,y,z in os.walk("files"):
            for b in y:
                x = x+"/"+b
                if x not in self.dirs:
                    self.dirs.append(x)
                    try:
                        sock = socket.socket()
                        sock.connect((self.host, self.port))
                        mkdir.mkdir(sock, x, self.username, self.password)
                        print "{0} Outgoing mkdir {1}".format(datetime.datetime.now(), x)
                    except Exception, e:
                        self.dirs.remove(x) # Remove it so that it is tried again later
                    time.sleep(0.5)

    def scanfiles(self):
        for root, dirs, files in os.walk("files"):
            for file_ in files:
                check = root+"/"+file_
                if check not in self.files:
                    try:
                        self.files[check] = hash(open(check).read()) 
                        sock = socket.socket()
                        sock.connect((self.host, self.port))
                        upload.upload(sock, check, self.username, self.password)
                        print "{0} Outgoing file transfer {1}".format(datetime.datetime.now(), check)
                    except Exception, e:
                        #print e
                        del self.files[check]
                    
                    time.sleep(0.5)

                else:
                    with open(check, 'rb') as file:
                        hashc = hash(file.read())
                        if hashc != self.files[check]:
                            try:
                                sock = socket.socket()
                                sock.connect((self.host, self.port))
                                upload.upload(sock, check, self.username, self.password)
                                print "{0} Outgoing file transfer {1}".format(datetime.datetime.now(), check)
                                self.files[check] = hash(open(check).read()) 
                            except Exception, e:
                                pass 
                            time.sleep(0.5)

    def shell(self):
        while True:
            cmd = "Shell> "
            cmd = raw_input(cmd)
            if cmd in self.usercmds:
                self.usercmds[cmd](self.host, self.port, self.username, self.password)
            
if __name__ == "__main__":
    Client().run()
