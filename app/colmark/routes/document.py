from flask_socketio import send, emit
from flask_socketio import join_room, leave_room
from main import socketio

DEFAULT_NAMESPACE = '/document'


@socketio.on('connect', namespace=DEFAULT_NAMESPACE)
def mouse_connect():
    print('Client connected')


@socketio.on('message', namespace=DEFAULT_NAMESPACE)
def handle_message(message):
    send(message)


@socketio.on('add', namespace=DEFAULT_NAMESPACE)
def handle_add(data):
    send(data)


@socketio.on('remove', namespace=DEFAULT_NAMESPACE)
def handle_remove(data):
    send(data)


@socketio.on('join', namespace=DEFAULT_NAMESPACE)
def on_join(data):
    print("hlleo world")
    username = data['username']
    document = data['document']
    join_room(document)
    send(username + ' has entered the room.', room=document)


@socketio.on('leave', namespace=DEFAULT_NAMESPACE)
def on_leave(data):
    username = data['username']
    document = data['document']
    leave_room(document)
    send(username + ' has left the room.', room=document)
