from django.utils.deprecation import MiddlewareMixin

from libs.app_logger import AppLogger

import datetime, json, uuid, django

logger = AppLogger(tag="DB connection handling middleware")


class DBConnectionHandler(MiddlewareMixin):

    def process_request(self, request):

        try:
            django.db.close_old_connections()
        except Exception as e:
            logger.error("Error. Reason: {}".format(e))

    def process_response(self, request, response):

        try:
            django.db.close_old_connections()
        except Exception as e:
            logger.error("Error. Reason: {}".format(e))
        return response
