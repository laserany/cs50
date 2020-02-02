import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = {}
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/channel", methods= ['POST'])
def create_channel():
    channels[f"{request.get_json()['channel']}"] = []
    return '', 201
@socketio.on('create_message')
def create_message(msg):
    if len(channels[f"{msg['channel']}"]) > 100:
        channels[f"{msg['channel']}"].pop(0)
    channels[f"{msg['channel']}"].append({"message": f"{msg['message']}", "display_name": f"{msg['display_name']}", "time_stamp": f"{msg['time_stamp']}"})
    emit('messages', {'messages': [chnl for chnl in channels[f"{msg['channel']}"]]}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)