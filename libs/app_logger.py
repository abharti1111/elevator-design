import logging


class AppLogger(object):

    def __init__(self, logger_type="primary", tag=None):
        self.logger = logging.getLogger(logger_type)
        self.tag = tag

    def info(self, message, tag=None, extra={}):
        if self.tag:
            extra['tag'] = self.tag
        extra['level'] = "INFO"
        self.logger.info(message, extra=extra)

    def error(self, message, tag=None, extra={}):
        if self.tag:
            extra['tag'] = self.tag
        extra['level'] = "ERROR"
        self.logger.error(message, extra=extra)

    def warn(self, message, tag=None, extra={}):
        if self.tag:
            extra['tag'] = self.tag
        extra['level'] = "WARN"
        self.logger.warn(message, extra=extra)

    def debug(self, message, tag=None, extra={}):
        if self.tag:
            extra['tag'] = self.tag
        extra['level'] = "DEBUG"
        self.logger.debug(message, extra=extra)
