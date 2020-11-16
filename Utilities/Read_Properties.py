import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\Config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseurl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

