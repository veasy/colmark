from flask_socketio import send, emit
from main import socketio


@socketio.on('message')
def handle_message(message):
    send(message)
