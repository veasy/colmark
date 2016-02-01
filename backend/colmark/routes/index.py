from flask import render_template
from colmark import config, app


@app.route('/test')
def root():
    return render_template('index.html', resources=config.WEB_STATIC_PATH)
