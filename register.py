from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import MySQLdb as mdb
from user import User
from db import DB
import yaml
import os



page_register = Blueprint('page_register', __name__,
                        template_folder='templates')

@page_register.route('/register', methods=["POST", "GET"])
def register():
    """ Let's read the config """
    with open(os.path.join(os.path.dirname(__file__), 'config.yaml'), 'r') as f:
        doc = yaml.load(f)

    """ Let's create the database object """
    db = DB(doc["database"]["host"], doc["database"]["user"], doc["database"]["pw"], doc["database"]["dbname"])

    mail_id = ''
    if request.method == 'POST':
        if request.form['mail_id'] != None and request.form['mail_pw'] != None:
            user = User(db, request.form['mail_id'], request.form['mail_pw'])
            user.save()

    return render_template('/pages/register.html', error=mail_id)