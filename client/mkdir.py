import json

def mkdir(obj, data, username, password):
    data = {"username":username, "password":password, "directory":data, "cmd":"mkdir"}
    obj.send(json.dumps(data))
    obj.close()
