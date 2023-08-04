#!/usr/bin/env python3
"""  Create a single / route and an index.html template
 that simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """ it returns 0-index.html"""
    return render_template('0-index.html')
