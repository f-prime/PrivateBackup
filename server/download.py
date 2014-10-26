import json
import base64
import zlib
import datetime

def download(obj, data, ip):
    print "{0} Outgoing file {1} to {2}".format(datetime.datetime.now(), data['file'], ip)
    data = base64.b64encode(zlib.compress(open(data['file']).read()))
    obj.send(data)
    obj.close()
