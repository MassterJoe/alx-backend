#!/usr/bin/env python3
""" configure the flask app and create a babe; object"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union
import pytz
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get locale function"""
    # locale from url parameter
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # locale from user settings
    user = g.user
    if user and locale in user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']

    # locale from request handler
    header = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header:
        return header

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """get user funtion"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """ Define a before_request function and use the
    app.before_request decorator to make it be
    executed before all other function """
    user = get_user()
    g.user = user


@babel.timezoneselector
def get_timezone():
    """ get time zone function """
    time_zone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    
    # 2. Timezone from user settings
    user = g.user
    if user and 'timezone' in user:
        try:
            pytz.timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass

    # 3. Default to UTC
    return 'UTC'


@app.route('/')
def get_index():
    """ Renders 1-index.html with custom data """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
