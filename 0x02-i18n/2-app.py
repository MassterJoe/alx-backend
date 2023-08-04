#!/usr/bin/env python3
""" configure the flask app and create a babe; object"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def get_index():
    """ Renders 1-index.html with custom data """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """ get locale function"""
    return request.accept_languages.best_match(app.Config['LANGUAGES'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
