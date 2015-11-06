from flask import Flask, request

app = Flask(__name__)

messages = {}
startpoint = {}
nextpoint = {}


@app.route("/post/<int:idx>/<message>/<int:pointx>", methods=["GET"])
def rec_post(idx, message, pointx):
    messages[idx]= message
    startpoint[idx] = nextpoint[idx]
    nextpoint[idx] = startpoint[idx] + len(message) + 1

@app.route("/read/startpoint/<int:idx>", methods=["GET"])
def get_startpoint(idx):
    if(idx not in startpoint):
        startpoint[idx] = 0
    return str(startpoint[idx])

@app.route("/read/message/<int:idx>", methods=["GET"])
def get_message(idx):
    return messages[int(idx)]

@app.route("/read/nextpoint/<int:idx>")
def get_nextpoint(idx):
    idx = int(idx)
    if(idx not in nextpoint):
        nextpoint[idx] = 0
    return str(nextpoint[idx])

app.run()