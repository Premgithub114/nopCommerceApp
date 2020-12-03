import logging
class log_gen:

    @staticmethod
    def log_data():

        logging.basicConfig(filename=".\\Logs\\log_data.log",
                          format="%(asctime)s:%(levelname)s:%(message)s",datefmt= "%m/%d/%y %I:%M:%S %P")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# Log file is not generating. Need to check later