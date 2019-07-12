import pymysql
import readConfig as readConfig
from Common.Log import MyLog as Log
localReadConfig = readConfig.ReadConfig()
import logging

class MyDB():
    def __init__(self):
        global username, password, port, database, config
        host = localReadConfig.get_db("host")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        port = localReadConfig.get_db("port")
        database = localReadConfig.get_db("database")
        config = {
            'host': str(host),
            'user': username,
            'passwd': password,
            'port': int(port),
            'db': database
        }

        self.log = Log.get_log()
        self.logger = logging.getLogger()
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            self.logger.info("Connect DB successfully!")
        except  Exception as ex:
            self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")

if __name__ == '__main__':
    A = MyDB()
    A.connectDB()