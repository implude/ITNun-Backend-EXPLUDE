import hashlib

def sha256_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()