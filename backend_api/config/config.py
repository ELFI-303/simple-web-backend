import os

class Config:
    @staticmethod
    def get_run_config():
        return os.environ.get('host'), os.environ.get('port')

    @staticmethod
    def get_database_config():
        return {
            "host": os.environ.get('mysqlHost'),
            "user": os.environ.get('mysqlUn'),
            "password": os.environ.get('mysqlRp'),
            "port": os.environ.get('mysqlPort'),
            "database": os.environ.get('mysqlDb')
        }