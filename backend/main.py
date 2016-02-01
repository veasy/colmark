import erc_config
from erc_server import socketio, app

if __name__ == '__main__':
    socketio.run(app=app, host='0.0.0.0',
                 port=erc_config.ERC_SERVER_PORT)
