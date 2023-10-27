import hashlib

def getSHA1(s):
    a=hashlib.sha1(s.encode("utf-8")).hexdigest().upper()
    return a