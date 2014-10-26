import json
import os
import datetime

def getDirs(obj, data, ip):
    dirs = []
    for x,y,z in os.walk("files"):
        dirs.append(x)

    for x,y,z in os.walk("files"):
        for b in y:
            x = x+"/"+b
            dirs.append(x)
    
    print "{0} Outgoing directory list to {1} with data {2}".format(datetime.datetime.now(), ip, dirs)
    obj.send(json.dumps({"data":dirs}))
    obj.close()
