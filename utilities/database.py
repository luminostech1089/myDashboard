import os
import sqlite3
import logging
import constants


class DBError(Exception):
    pass

class DB:
    def __init__(self, timeout=600):
        self.__databaseName = os.path.join(constants.UTILS_DIR, 'database.db')
        self.timeout = timeout
        self.conn = None
        self.cursor = None

    def connect(self):
        logging.debug("Connecting to database")
        self.conn = sqlite3.connect(self.__databaseName, timeout=self.timeout)
        self.cursor = self.conn.cursor()

    def close(self):
        logging.debug("Closing database connection")
        if self.conn:
            self.conn.close()

    @property
    def db(self):
        return self.__databaseName

    def execute(self, *args, **kwargs):
        if not self.cursor:
            self.connect()
        try:
            logging.debug("DB query {}".format(args))
            if kwargs:
                params = "{}".format((key, value) for key, value in kwargs.iteritems())
                logging.debug("Query Arguments: {}".format(params))
            output = self.cursor.execute(*args, **kwargs)
            self.conn.commit()
            return output
        except Exception as err:
            print "**error-{}".format(err)
            logging.info("Failed to execute DB query. Error - {}".format(err), exc_info=True)
            raise DBError("Error occurred while executing DB query")


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
    db.execute("SELECT user FROM USERS")
    db.close()




if __name__  == "__main__":
    from utilities.logger import ConsoleLogger
    ConsoleLogger()
    db = DB()
    #db.execute("DROP TABLE USERS;")
    #create_default_user()
    op = db.execute("SELECT * FROM USERS WHERE user=='root'")
    print op.fetchone()
    db.close()


