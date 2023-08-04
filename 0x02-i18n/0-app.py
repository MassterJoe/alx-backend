from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index1():
    """ Renders 0-index.html with custom data """
    page_title = "Welcome to Holberton"
    header = "Hello world"
    return render_template('0-index.html',
                           page_title=page_title, header=header)


@app.route('/index2')
def index2():
    """ Renders 1-index.html with custom data """
    page_title = "This is the second page"
    header = "This is the second page"
    return render_template('1-index.html',
                           page_title=page_title, header=header)
