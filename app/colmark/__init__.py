from flask import Flask
from flask_socketio import SocketIO
from config import WEB_STATIC_PATH, WEB_TEMPLATE_PATH

app = Flask(__name__,
            static_folder=WEB_STATIC_PATH,
            template_folder=WEB_TEMPLATE_PATH)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'secret!'
app.debug = True

# import routes
import colmark.routes.index
