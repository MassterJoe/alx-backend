#!/usr/bin/env python3
""" configure the flask app and create a babe; object"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """get user funtion"""
    login_id = request.args.get('login_as')
    if login_id is None or not login_id.isdigit():
        return None

    login_id = int(login_id)
    user = users.get(login_id)
    return user


@app.before_request
def before_request():
    """ Define a before_request function and use the
    app.before_request decorator to make it be
    executed before all other function """
    user = get_user()
    g.user = user


@app.route('/')
def get_index():
    """ Renders 1-index.html with custom data """
    user = g.user
    return render_template('5-index.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
