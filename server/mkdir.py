import os

def mkdir(obj, data, ip):
    directory = "{0}".format(data['directory'])
    try:
        if not os.path.exists("files"):
            os.mkdir("files")
        os.mkdir(directory)
    except OSError:
        pass
