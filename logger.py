import logging
import os


class LoggerMixin:
    LOG_FORMAT = os.environ.get(
        'LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    LOG_LEVEL = logging.getLevelName(
        os.environ.get('LOG_LEVEL', logging.DEBUG))

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(self.LOG_LEVEL)
        sh = logging.StreamHandler()
        sh.setLevel(self.LOG_LEVEL)
        sh.setFormatter(logging.Formatter(self.LOG_FORMAT))
        self.logger.addHandler(sh)
