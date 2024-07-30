#!/usr/bin/env python3
''' basic flask app'''
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(config)

babel = Babel(app)

@app.route('/')
def get_index():
    '''index page'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)