'''
This is the chat client wallflower; it connects currently to a server hosted by CaveFox Telecommunications; but that
can be changed to any server hosting the Wallflower_Server.py software package.
'''
import pickle
import requests
import time
import threading
import hashlib
message = ''
startpoint = 0
endpoint = 0
print('                 Project Wallflower')
print('      One-Time Pad Cryptography Chat Software')
print('(c)2015 Michael Canning - CaveFox Telecommunications')
print('----------------------------------------------------')
print('All text is converted to lowercase, only letters and : are supported')
print('[System] - Loading One-Time Pad...')
pad = open("crypto.pad", 'r')  # Loads the one time pad
pad = pickle.load(pad)
print('[System] - Loaded...')
username = str(raw_input("Desired Username: "))
ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ":"]


def md5(fname):  # This is used to get a had of the pad
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


def encrypt(message, startpoint):  # Encrypts the message
    encoded = []
    # Adds numbers to 'encoded' array based on the letter
    for char in message.lower(): # Loops through input
        for alphabetIndex in range(1, len(ALPHABET)): # Loops through alphabet
            if char is ALPHABET[alphabetIndex - 1]: # Converts that letter to its matching number
                encoded.append(alphabetIndex)
                break

    # z = 0 # This line seems useless but I was scared to delete it
    final = ''
    for num in encoded: # Loops through each number
        encrypted = (x + pad[startpoint]) % 28 # Pad cipher
        final = final + ALPHABET[num - 1] # Gets corresponding letter

        startpoint = startpoint + 1

    return final, startpoint

def decrypt(message, startpoint):  # Decrypts the message
    encoded = []
    for x in message.lower():
        if x is 'a':
            encoded.append(1)
        if x is 'b':
            encoded.append(2)
        if x is 'c':
            encoded.append(3)
        if x is 'd':
            encoded.append(4)
        if x is 'e':
            encoded.append(5)
        if x is 'f':
            encoded.append(6)
        if x is 'g':
            encoded.append(7)
        if x is 'h':
            encoded.append(8)
        if x is 'i':
            encoded.append(9)
        if x is 'j':
            encoded.append(10)
        if x is 'k':
            encoded.append(11)
        if x is 'l':
            encoded.append(12)
        if x is 'm':
            encoded.append(13)
        if x is 'n':
            encoded.append(14)
        if x is 'o':
            encoded.append(15)
        if x is 'p':
            encoded.append(16)
        if x is 'q':
            encoded.append(17)
        if x is 'r':
            encoded.append(18)
        if x is 's':
            encoded.append(19)
        if x is 't':
            encoded.append(20)
        if x is 'u':
            encoded.append(21)
        if x is 'v':
            encoded.append(22)
        if x is 'w':
            encoded.append(23)
        if x is 'x':
            encoded.append(24)
        if x is 'y':
            encoded.append(25)
        if x is 'z':
            encoded.append(26)
        if x is ' ':
            encoded.append(27)
        if x is ':':
            encoded.append(28)
    z = 0
    final = ''
    for x in encoded:
        decryptic = x - pad[startpoint]
        decryptic = decryptic % 28
        startpoint = startpoint + 1
        if decryptic is 1:
            final = final + 'a'
        if decryptic is 2:
            final = final + 'b'
        if decryptic is 3:
            final = final + 'c'
        if decryptic is 4:
            final = final + 'd'
        if decryptic is 5:
            final = final + 'e'
        if decryptic is 6:
            final = final + 'f'
        if decryptic is 7:
            final = final + 'g'
        if decryptic is 8:
            final = final + 'h'
        if decryptic is 9:
            final = final + 'i'
        if decryptic is 10:
            final = final + 'j'
        if decryptic is 11:
            final = final + 'k'
        if decryptic is 12:
            final = final + 'l'
        if decryptic is 13:
            final = final + 'm'
        if decryptic is 14:
            final = final + 'n'
        if decryptic is 15:
            final = final + 'o'
        if decryptic is 16:
            final = final + 'p'
        if decryptic is 17:
            final = final + 'q'
        if decryptic is 18:
            final = final + 'r'
        if decryptic is 19:
            final = final + 's'
        if decryptic is 20:
            final = final + 't'
        if decryptic is 21:
            final = final + 'u'
        if decryptic is 22:
            final = final + 'v'
        if decryptic is 23:
            final = final + 'w'
        if decryptic is 24:
            final = final + 'x'
        if decryptic is 25:
            final = final + 'y'
        if decryptic is 26:
            final = final + 'z'
        if decryptic is 27:
            final = final + ' '
        if decryptic is 0:
            final = final + ':'
    return final, startpoint

class getmessage(threading.Thread):  # Thread to get the latest message every second; time can be change to faster or slower
    def __init__(self, id):
        self.id = id
        threading.Thread.__init__(self)

    def run(self):
        messagecheck = ''
        flag = 0
        while True:
            time.sleep(1)
            r = requests.get('http://198.100.155.138:5000/read/startpoint/' + str(id))
            startpoint = int(r.text)
            r = requests.get('http://198.100.155.138:5000/read/message/' + str(id))
            cryptic = str(r.text)
            if (cryptic != messagecheck):
                if (flag >= 5):
                    r = requests.get('http://198.100.155.138:5000/read/nextpoint/' + str(id))
                    nextpoint = int(r.text)
                    print('[System] - ' + str(float((len(pad) - nextpoint - 1))/float(len(pad))) + "% of Pad Used")
                    flag = 0
                else:
                    flag = flag + 1
                message, trash = decrypt(cryptic, startpoint)
                print "[Channel] - " + message
                messagecheck = cryptic

class sendmessage(threading.Thread):  # Sends messages with a thread, and also sends the join server message
    def __init__(self, id):
        self.username = username
        self.id = id
        r = requests.get('http://198.100.155.138:5000/read/nextpoint/' + str(id))
        startpoint = int(r.text)
        print('[System] - You are chatting securely on channel: [' + str(id) + ']')
        cryptic, startpointx = encrypt(self.username + " Has Joined!", startpoint)
        requests.get("http://198.100.155.138:5000/post/" + str(id) + "/" + str(cryptic) + "/" + str(len('A User Has Joined')))
        threading.Thread.__init__(self)
    def run(self):
        while True:
            message = str(raw_input('Message: \n'))
            r = requests.get('http://198.100.155.138:5000/read/nextpoint/' + str(id))
            startpoint = int(r.text)
            cryptic, startpointx = encrypt(self.username + ' : ' + message, startpoint)
            requests.get("http://198.100.155.138:5000/post/" + str(id) + "/" + str(cryptic) + "/" + str(len(message)))

id = abs(int(hash(md5('crypto.pad'))))  # Hashes the Pad to connect to the channel for it on the server
getmessage(id).start()  # Starts the message get thread
sendmessage(id).start()  # Starts the message send thread
