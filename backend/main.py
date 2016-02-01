from colmark import config, socketio, app

if __name__ == '__main__':
    socketio.run(app, port=config.SERVER_PORT)
