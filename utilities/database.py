import sqlite3


class DB:
    def __init__(self, timeout=600):
        print "Connecting to database"
        self.conn = sqlite3.connect('database.db', timeout=timeout)
        self.cursor = self.conn.cursor()

    def close(self):
        print "closing database connection"
        self.conn.close()

    def execute(self, *args, **kwargs):
        try:
            output = self.cursor.execute(*args, **kwargs)
            self.conn.commit()
            return output
        except Exception as err:
            print "Failed to execute query due to error - {}".format(err)
            self.close()
            raise


def create_default_user():
    db = DB()
    user = "root"
    pwd = "root"
    usersTable = """CREATE TABLE IF NOT EXISTS USERS
             (id integer PRIMARY KEY NOT NULL,
              user test NOT NULL,
              pwd text NOT NULL
             );"""
    addUser = "INSERT INTO USERS(id, user, pwd) VALUES (?, ?, ?)"
    db.execute(usersTable)
    userdata = (1, 'root', 'root')
    db.execute(addUser, userdata)
    db.close()




if __name__  == "__main__":
    db = DB()
    # db.execute("DROP TABLE USERS;")
    #create_default_user()
    op = db.execute("SELECT * FROM USERS")
    for data in op:
        print data
    db.close()

