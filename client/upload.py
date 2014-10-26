import json
import base64
import zlib

def upload(obj, data, username, password):
    json_ = {"cmd":"upload", "data":base64.b64encode(zlib.compress(open(data).read())), "username":username, "password":password, "name":data}
    obj.send(json.dumps(json_))
    obj.close()
