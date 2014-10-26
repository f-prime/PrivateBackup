import base64
import zlib

def upload(obj, data, ip):
    name = "{0}".format(data['name'])
    with open(name, 'wb') as file:
        file.write(zlib.decompress(base64.b64decode(data['data'])))
    
