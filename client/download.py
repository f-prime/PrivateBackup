import socket
import json
import datetime
import zlib
import base64
import os

def download(host, port, username, password):
    dirs = getDirs(host, port, username, password)
    for x in dirs['data']:
        try:
            os.mkdir(x)
        except Exception, e:
            pass

    print "{0} Incoming from {1} with data {2}".format(datetime.datetime.now(), host, dirs)
    files = getFiles(host, port, username, password)
    print "{0} Incoming from {1} with data {2}".format(datetime.datetime.now(), host, files)
    for x in files['data']:
        print x
        s = socket.socket()
        s.connect((host, port))
        s.send(json.dumps({"username":username, "password":password, "cmd":"download", "file":x}) + " EOT")
        data = ""
        while True:
            d = s.recv(1024)
            if not d:
                break
            data += d
        print "{0} Incoming file from {1} with name {2}".format(datetime.datetime.now(), host, x)
        with open(x, 'wb') as file:
            file.write(zlib.decompress(base64.b64decode(data)))
        s.close()

def getFiles(host, port, username, password):
    s = socket.socket()
    s.connect((host, port))
    data = json.dumps({"username":username, "password":password, "cmd":"getFiles"})
    s.send(data + " EOT")
    data = ""
    while True:
        d = s.recv(1024)
        if d:
            data += d
        else:
            break

    return json.loads(data)


def getDirs(host, port, username, password):
    s = socket.socket()
    s.connect((host, port))
    data = json.dumps({"username":username, "password":password, "cmd":"getDirs"})
    s.send(data + " EOT")
    data = ""
    while True:
        d = s.recv(1024)
        if d:
            data += d
        else:
            break

    return json.loads(data)
