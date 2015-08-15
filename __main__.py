from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from random import randint


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template('/pages/login.html')

if (__name__) == '__main__':
    app.run()