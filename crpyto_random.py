from base64 import b64encode
import os


def randint():
    random = abs(hash((b64encode(os.urandom(64)).decode('utf-8')).lower()))
    return random
