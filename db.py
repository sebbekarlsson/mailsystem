import MySQLdb as mdb


class DB(object):
    host = ''
    user = ''
    pw = ''
    dbname = ''

    def __init__(self, host, user, pw, dbname):
        self.host = host
        self.user = user
        self.pw = pw
        self.dbname = dbname

        self.connection = mdb.connect(self.host, self.user, self.pw, self.dbname);

    def query(self, query):
        cursor = self.connection.cursor()
        result = cursor.execute(query)
        self.connection.commit()

        return result