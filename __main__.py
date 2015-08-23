from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from random import randint
import MySQLdb as mdb
from user import User
from db import DB
import yaml
import os
from register import page_register


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.register_blueprint(page_register)

""" Let's read the config """
with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as f:
    doc = yaml.load(f)

""" Let's create the database object """
db = DB(doc["database"]["host"], doc["database"]["user"], doc["database"]["pw"], doc["database"]["dbname"])

def main():
    global db

    setup_database(db)
    app.run(host="localhost", port=25565)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    error = ''
    return render_template('/pages/login.html', error=error)


def setup_database(db):
    db.query("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTO_INCREMENT, mail_id varchar(64), mail_pw varchar(64))")

if (__name__) == '__main__':
    main()




