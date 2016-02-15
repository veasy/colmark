from flask import Flask, g
from flask_socketio import SocketIO
from peewee import SqliteDatabase

from colmark import config

app = Flask(__name__,
            static_url_path=config.WEB_STATIC_PATH,
            static_folder=config.WEB_STATIC_FOLDER,
            template_folder=config.WEB_TEMPLATE_PATH)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'secret!'
app.debug = True

# database
database = SqliteDatabase(config.DATABASE_NAME)

# import routes
import colmark.routes.index
import colmark.routes.document
import colmark.routes.error_handling