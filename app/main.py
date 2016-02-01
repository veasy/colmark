from colmark import config
from colmark import socketio, app

if __name__ == '__main__':
    socketio.run(app, port=config.SERVER_PORT, host='0.0.0.0', log_output=True, debug=True)
