import logging
import constants as const
from utilities.database import DB


class AppDb:
    def __init__(self):
        self.__db = DB()

    def createDefaultUser(self):
        createTableQ = """CREATE TABLE USERS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                          user TEXT NOT NULL,
                          pwd TEXT NOT NULL
                       );"""
        addUserQ = "INSERT INTO USERS (user, pwd) VALUES (?, ?);"
        self.execute(createTableQ)
        userdata = (const.DEFAULT_DB_USER, const.DEFAULT_DB_PWD)
        self.execute(addUserQ, userdata)

    def execute(self, *args, **kwargs):
        return self.__db.execute(*args, **kwargs)

    def getUserDetails(self, username):
        result = self.execute("SELECT user,pwd FROM USERS WHERE user='{}';".format(username))
        return result.fetchone() if result else None



if __name__ == "__main__":
    from utilities.logger import ConsoleLogger
    ConsoleLogger()
    a = AppDb()
