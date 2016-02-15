from colmark.app import socketio
from flask import request


@socketio.on_error_default
def default_error_handler(e):
    print(request.event["message"])
    print(request.event["args"])
