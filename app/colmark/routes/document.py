from flask_socketio import send, emit
from flask_socketio import join_room, leave_room
from main import socketio


@socketio.on('message')
def handle_message(message):
    send(message)


@socketio.on('add')
def handle_add(data):
    send(data)


@socketio.on('remove')
def handle_remove(data):
    send(data)


@socketio.on('join')
def on_join(data):
    username = data['username']
    document = data['document']
    join_room(document)
    send(username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    document = data['document']
    leave_room(document)
    send(username + ' has left the room.', room=room)
