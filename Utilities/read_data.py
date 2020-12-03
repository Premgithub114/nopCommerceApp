import configparser
conf = configparser.RawConfigParser()
conf.read("C:/Users/Prem/PycharmProjects/Hybrid_FW/Configuration/config.ini")

class all_data:
    @staticmethod
    def get_url():
        url = conf.get("data","url")
        return url

    @staticmethod
    def get_user_email():
        email = conf.get("data", "user_email")
        return email

    @staticmethod
    def get_passw():
        password = conf.get("data", "user_pass")
        return password
