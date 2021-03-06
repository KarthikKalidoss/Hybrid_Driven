import logging
import io
from io import StringIO


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\CAF.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


