from flask_socketio import emit
from flask_socketio import join_room, leave_room
from main import socketio

DOCUMENT_NAMESPACE = '/document'


@socketio.on('connect', namespace=DOCUMENT_NAMESPACE)
def on_connect():
    print('Client connected')


@socketio.on('disconnect', namespace=DOCUMENT_NAMESPACE)
def on_disconnect():
    print('Client disconnected')


@socketio.on('message', namespace=DOCUMENT_NAMESPACE)
def handle_message(message):
    print('MSG: %s' % message)


@socketio.on('echo', namespace=DOCUMENT_NAMESPACE)
def handle_echo(message):
    print('ECHO: %s' % message)
    emit('echo', 'This was your message: %s' % message)


@socketio.on('add', namespace=DOCUMENT_NAMESPACE)
def handle_add(data):
    print('Add: %s' % data)
    emit('update', data['add'], broadcast=True)


@socketio.on('remove', namespace=DOCUMENT_NAMESPACE)
def handle_remove(data):
    print('Remove: %s' % data)


@socketio.on('join', namespace=DOCUMENT_NAMESPACE)
def on_join(data):
    username = data['username']
    document = data['document']
    join_room(document)
    print ('%s has entered the room (%s).' % (username, document))

    # broadcast new userlist and send back current document
    emit('userlist', ['Markus', username], room=document)
    emit('document', 'Lorem ipsum dolor sit amet')


@socketio.on('leave', namespace=DOCUMENT_NAMESPACE)
def on_leave(data):
    username = data['username']
    document = data['document']
    leave_room(document)
    print ('%s has left the room (%s).' % (username, document))
