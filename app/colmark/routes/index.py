from colmark import app
from flask import render_template
from colmark import config


@app.route('/')
def root():
    render_template('index', resources=config.WEB_STATIC_PATH)
