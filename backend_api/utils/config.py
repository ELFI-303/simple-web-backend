import os

class Config:
    @staticmethod
    def get_run_config():
        return os.environ.get('host'), os.environ.get('port')

    @staticmethod
    def get_mysql_config():
        return {
            "host": os.environ.get('mysqlHost'),
            "user": os.environ.get('mysqlUn'),
            "password": os.environ.get('mysqlRp'),
            "port": os.environ.get('mysqlPort'),
            "database": os.environ.get('mysqlDb')
        }
    
    @staticmethod
    def api_path():
        return "/api/v1/"
    
    @staticmethod
    def api_mail():
        return {
            "sendMail":os.environ.get('sendMail'),
            "sendPass":os.environ.get('sendPass'),
            "receiver":os.environ.get('receiver')
        }