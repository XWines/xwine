from decouple import config
import json
import logging

from flask import Flask
from flask_mongoengine import MongoEngine

from app.logger import AppLogger

mongo = MongoEngine()
from app.api.urls import api

log = AppLogger()


class BaseConfig:
    """Base Configuration"""
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', cast=bool)
    MONGODB_SETTINGS = json.loads(config('MONGODB_SETTINGS'))
    MONGODB_SETTINGS["retryWrites"] = False
    MONGODB_SETTINGS["connect"] = False
    REDIS_URL = config('REDIS_URL')


def register_blueprint(app):
    app.register_blueprint(api)


def KnockKnock():
    log.info("This is being logged knockknock")
    return {
        "message": "Hello from document-service!"
    }


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    mongo.init_app(app)
    register_blueprint(app)
    app.add_url_rule("/knockknock",
                     view_func=KnockKnock)
    return app


def create_worker_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    mongo.init_app(app)
    return app
