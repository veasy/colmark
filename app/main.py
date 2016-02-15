from colmark import config
from colmark.app import socketio, app, database
from colmark.model.document import Document
from colmark.model.user import User

if __name__ == '__main__':
    # create database
    database.create_tables([User, Document], safe=True)
    socketio.run(app, port=config.SERVER_PORT, host='0.0.0.0', log_output=True, debug=True)
