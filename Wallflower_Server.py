'''
This is the server for hosting chat. The server stores messages in encrypted form, and the start and next point
on the pad.
'''
from flask import Flask
import pickle
import os

app = Flask(__name__)

messages = {}
startpoint = {}
nextpoint = {}


def savepoint(idx): # Saves start and end points in key pad to protect for fallback attacks after server restart
    f = open('chandata/' + str(idx) + 'start.point', 'w')
    pickle.dump(startpoint[idx], f)
    f = open('chandata/' + str(idx) + 'next.point', 'w')
    pickle.dump(nextpoint[idx], f)


def loadpoint(idx):  # Loads start point of the current message and next point in the pad
    if idx in startpoint:
        return
    elif os.path.isfile('chandata/' + str(idx) + 'start.point'):
        startx = open('chandata/' + str(idx) + "start.point", 'r')
        startpoint[idx] = pickle.load(startx)
        nextx = open('chandata/' + str(idx) + "next.point", 'r')
        nextpoint[idx] = pickle.load(nextx)
    else:
        startpoint[idx] = 0
        nextpoint[idx] = 0


@app.route("/post/<int:idx>/<message>/<int:pointx>", methods=["GET"])
def rec_post(idx, message, pointx):  # Saves post from channel to an array
    messages[idx]= message
    startpoint[idx] = nextpoint[idx]
    nextpoint[idx] = startpoint[idx] + len(message) + 1
    savepoint(idx)

@app.route("/read/startpoint/<int:idx>", methods=["GET"])  #Provides client with the point where the message starts in the pad
def get_startpoint(idx):
    loadpoint(idx)
    return str(startpoint[idx])

@app.route("/read/message/<int:idx>", methods=["GET"])  # Provides latest message to client
def get_message(idx):
    return messages[int(idx)]

@app.route("/read/nextpoint/<int:idx>")  # Provides vlient with where the next message should start on the pad
def get_nextpoint(idx):
    loadpoint(idx)
    return str(nextpoint[idx])

app.run(host="0.0.0.0")
