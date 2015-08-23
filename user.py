import MySQLdb as mdb


class User(object):
    mail_id = ''
    mail_pw = ''

    def __init__(self, db, mail_id, mail_pw):
        self.mail_id = mail_id
        self.mail_pw = mail_pw
        self.db = db

    def save(self):
        self.db.query("INSERT INTO users (mail_id, mail_pw) VALUES('"+self.mail_id+"', '"+self.mail_pw+"')")
        