#!/usr/bin/env python3
"""  Create a single / route and an index.html template
 that simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)."""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    app.config['LANGUAGES'] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


babel = Babel(app)


@app.route('/')
def index1():
    """ it returns 0-index.html"""
    return render_template('0-index.html')


@app.route('/index2')
def index2():
    return render_template('1-index.html')
