from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    login_as = request.args.get('login_as')
    if login_as:
        user_id = int(login_as)
        return users.get(user_id)
    return None


def set_locale():
    # Priority: URL parameter -> user setting ->
    # request header -> default locale
    url_locale = request.args.get('lang')
    if url_locale:
        return url_locale

    if g.user and g.user.get('locale'):
        return g.user.get('locale')

    return request.accept_languages.best_match(['en', 'fr']) or 'en'


@app.before_request
def before_request():
    g.user = get_user()
    g.locale = set_locale()  # Set the locale globally


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
