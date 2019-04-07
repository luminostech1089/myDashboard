import sqlite3


class DB:
    def __init__(self, timeout=600):
        print "Connecting to database"
        self.conn = sqlite3.connect('database.db', timeout=timeout)
        self.cursor = self.conn.cursor()

    def close(self):
        print "closing database connection"
        self.conn.close()

    def execute(self, query):
        print "Executing a query {}".format(query)
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as err:
            print "Failed to execute query due to error - {}".format(err)
            self.close()
            raise


def create_default_user():
    db = DB()
    user = "root"
    pwd = "root"
    usersTable = '''CREATE TABLE USERS
             (ID INT PRIMARY KEY     NOT NULL,
              USER           TEXT    NOT NULL,
              PASSWORD       TEXT     NOT NULL
             );'''
    addUser = "INSERT INTO USERS (ID, USER, PASSWORD) VALUES (1, {} {}".format(user, pwd)
    db.execute(usersTable)
    db.execute(addUser)
    db.close()




if __name__  == "__main__":
    db = DB()
    #create_default_user()
    op = db.execute("SELECT ID, USER, PASSWORD from USERS")
    print op
    db.close()

