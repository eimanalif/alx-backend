#!/usr/bin/env python3
"""
A Basic Flask application for internationalization (i18n) using Flask-Babel.
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class AppConfig:
    """Configuration class for application"""
    SUPPORTED_LANGUAGES = ['en', 'fr']
    DEFAULT_LANGUAGE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


# Create an instance of Flask
my_app = Flask(__name__)
# Load configuration from the AppConfig class
my_app.config.from_object(AppConfig)


# Initialize Babel for internationalization
babel = Babel(my_app)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request object"""
    return request.accept_languages.best_match(
        my_app.config['SUPPORTED_LANGUAGES'])


@my_app.route('/', strict_slashes=False)
def display_index() -> str:
    """Render a basic HTML template"""
    return render_template('3-index.html')


if __name__ == '__main__':
    # Change the host and port for production
    my_app.run(host='0.0.0.0', port=5000)
