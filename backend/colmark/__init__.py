from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

app.config['SECRET_KEY'] = 'secret!'
app.debug = True

# import routes
import colmark.routes.index
import colmark.routes.document
