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
def index()
    return "Hello, World!"


if __name__ = "__main__":
    app.run(debug=True)
