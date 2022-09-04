"""
Logging Config, imported at the end of common.py
"""
import os
import json_log_formatter
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

HOST_NAME = os.getenv('HOSTNAME')


class CustomJsonFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message, extra, record):
        request = extra.pop('request', None)
        extra["level"] = record.levelname
        extra["message"] = record.getMessage()
        extra["caller"] = record.filename + '::' + record.funcName
        extra['logger_name'] = record.name
        extra['module'] = record.module
        extra['funcName'] = record.funcName
        extra['filename'] = record.filename
        extra['lineno'] = record.lineno
        extra['thread'] = record.threadName
        extra['pid'] = record.process
        extra['application_name'] = "elevator_design"

        return super(CustomJsonFormatter, self).json_record(message, extra, record)


class RequestResponseFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message, extra, record):
        request = extra.pop('request', None)
        record_dict = record.__dict__.items()
        record_msg_list = list(record_dict)[1][1]
        extra["execution_time"] = record_msg_list['execution_time']
        extra["ip_address"] = record_msg_list['ip_address']
        extra["method"] = record_msg_list['request']['method']
        extra["full_path"] = record_msg_list['request']['full_path']
        extra["query_params"] = record_msg_list['request']['query_params']
        extra["req_params"] = record_msg_list['request']['data']
        extra["status_code"] = record_msg_list['response']['status_code']
        if record_msg_list['response'].get('data'):
            extra["data"] = json.loads(record_msg_list['response'].get('data', "{}"))
        extra["level"] = record.levelname
        extra["caller"] = record.filename + '::' + record.funcName
        extra['logger_name'] = record.name
        extra['module'] = record.module
        extra['funcName'] = record.funcName
        extra['filename'] = record.filename
        extra['lineno'] = record.lineno
        extra['thread'] = record.threadName
        extra['pid'] = record.process
        extra['application_name'] = "elevator_design"

        return super(RequestResponseFormatter, self).json_record({}, extra, record)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter',
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s %(request_id)s',
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(message)s %(request_id)s',
        },
        'json': {
            '()': CustomJsonFormatter
        },
        'req-resp-json': {
            '()': RequestResponseFormatter
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'json',
            'filters': ['request_id'],
        },
        'django_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            "maxBytes": 50000000,
            "backupCount": 10,
            'formatter': 'req-resp-json',
            'filename': os.path.join(LOG_DIR, 'elevator_design_service_' + HOST_NAME + '_django.log'),
            'filters': ['request_id'],
        },
        'exceptions_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            "maxBytes": 50000000,
            "backupCount": 10,
            'formatter': 'json',
            'filename': os.path.join(LOG_DIR, 'elevator_design_service_' + HOST_NAME + '_exceptions.log'),
            "encoding": "utf8",
            'filters': ['request_id'],
        },
        'primary_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            "maxBytes": 50000000,
            "backupCount": 10,
            'formatter': 'json',
            'filename': os.path.join(LOG_DIR, 'elevator_design_service_' + HOST_NAME + '_primary.log'),
            'filters': ['request_id'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['exceptions_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'primary': {
            'handlers': ['primary_file'],
            'level': 'DEBUG',
        },
        'requestlogs': {
            'handlers': ['django_file'],
            'level': 'DEBUG',
            'propagate': False,
        },

    },
}
