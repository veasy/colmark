from colmark import app
from flask import render_template
from colmark import config


@app.route('/')
def root():
    return render_template('index.html', resource=config.WEB_STATIC_PATH)
