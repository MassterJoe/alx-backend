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
    return render_template('0-index.html')


@app.route('/index2')
def index2():
    """ Renders 1-index.html with custom data """
    return render_template('1-index.html')
