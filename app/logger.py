import logging
from logging.config import dictConfig

from decouple import config


def setup_logging():
    debug = config('DEBUG', cast=bool)

    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            # "default": {
            #     "format": '{"time":"%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "message":"%(message)s"}',
            # },
            "default": {
                "format": "%(message)s",
            }
        },
        "handlers": {
            "console": {
                "level": "INFO",
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
            "email": {
                "class": "logging.handlers.SMTPHandler",
                "formatter": "default",
                "level": "ERROR",
                "mailhost": ("smtp.example.com", 587),
                "fromaddr": "devops@example.com",
                "toaddrs": ["receiver@example.com", "receiver2@example.com"],
                "subject": "Error Logs",
                "credentials": ("username", "password"),
            },
            # "slack": {
            #     "class": "app.HTTPSlackHandler",
            #     "formatter": "default",
            #     "level": "ERROR",
            # },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "default",
                "filename": "/var/log/ind-documents/documents-uwsgi.log" if not debug else "documents-uwsgi.log",
                "maxBytes": 0,
                "backupCount": 0,
                "level": "INFO",
                "mode": "a"
            }
        },
        # "loggers": {
        #     "gunicorn.error": {
        #         "handlers": ["console"] if debug else ["console", "slack", "error_file"],
        #         "level": "INFO",
        #         "propagate": False,
        #     },
        #     "gunicorn.access": {
        #         "handlers": ["console"] if debug else ["console", "access_file"],
        #         "level": "INFO",
        #         "propagate": False,
        #     }
        # },
        "root": {
            "level": "DEBUG" if debug else "INFO",
            "handlers": ["console", "error_file"] if debug else ["error_file"],
        }
    })


class AppLogger:
    def __init__(self):
        # setup_logging()
        self.logger = logging.getLogger(__name__)

    def info(self, msg='', user_id=''):
        self.logger.info(
            {'message': msg, "user_id": str(user_id)}, exc_info=False
        )

    def error(self, msg, user_id=''):
        self.logger.error(
            {"user_id": str(user_id), 'message': msg}, exc_info=False
        )

    def warning(self, msg, user_id=''):
        self.logger.warning(
            {"user_id": str(user_id), 'message': msg}, exc_info=False
        )

    def debug(self, msg, user_id=''):
        self.logger.debug(
            {"user_id": str(user_id), 'message': msg}, exc_info=False
        )
