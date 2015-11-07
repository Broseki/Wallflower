from flask import Flask
import pickle
import os

app = Flask(__name__)

messages = {}
startpoint = {}
nextpoint = {}


def savepoint(idx):
    f = open('chandata/' + str(idx) + 'start.point', 'w')
    pickle.dump(startpoint[idx], f)
    f = open('chandata/' + str(idx) + 'next.point', 'w')
    pickle.dump(nextpoint[idx], f)


def loadpoint(idx):
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
def rec_post(idx, message, pointx):
    messages[idx]= message
    startpoint[idx] = nextpoint[idx]
    nextpoint[idx] = startpoint[idx] + len(message) + 1
    savepoint(idx)

@app.route("/read/startpoint/<int:idx>", methods=["GET"])
def get_startpoint(idx):
    loadpoint(idx)
    return str(startpoint[idx])

@app.route("/read/message/<int:idx>", methods=["GET"])
def get_message(idx):
    return messages[int(idx)]

@app.route("/read/nextpoint/<int:idx>")
def get_nextpoint(idx):
    loadpoint(idx)
    return str(nextpoint[idx])

app.run(host="0.0.0.0")
