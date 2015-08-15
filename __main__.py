from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from random import randint
import MySQLdb as mdb


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def main():
    setup_database()
    app.run()

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    error = 'There was an error'
    return render_template('/pages/login.html', error=error)

def setup_database():
    con = mdb.connect('localhost', 'root', 'tango255', 'mailsystem');

    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTO_INCREMENT, mail_id varchar(64), mail_pw varchar(64))")

if (__name__) == '__main__':
    main()




