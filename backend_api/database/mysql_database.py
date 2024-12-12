from mysql.connector import connect
from utils.config import Config

class MySQLDatabase:
    def __init__(self):
        self.config = Config.get_mysql_config()

    def get_db(self):
        db = connect(**self.config)
        return db