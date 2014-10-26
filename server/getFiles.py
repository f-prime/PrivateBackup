import time
import datetime
import os
import json

def getFiles(obj, data, ip):
    files = []
    for x,_,z, in os.walk("files"):
        for f in z:
            data = x + "/" + f
            files.append(data)

    output = json.dumps({"data":files})
    print "{0} Outgoing to {1} with data {2}".format(datetime.datetime.now(), ip, output)
    obj.send(output)
    obj.close()
