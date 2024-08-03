#!/usr/bin/env python3
"""Basic Flask app with internationalization support"""
from flask_babel import Babel, gettext as _
from flask import Flask, render_template, request


class Config:
    """Represents Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves locale for web page"""
    return request.args.get('lang', 'en')


@app.route('/')
def get_index() -> str:
    """index page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
