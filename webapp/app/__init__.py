from flask import Flask
import logging

log = logging.getLogger('werkzeug')
log.disabled = True


class Logger:
    @staticmethod
    def info(message):
        print(f"\033[34m[*]\033[0m {message}")

    @staticmethod
    def success(message):
        print(f"\033[32m[+]\033[0m {message}")

    @staticmethod
    def debug(message):
        print(f"\033[33m[^]\033[0m {message}")

    @staticmethod
    def error(message):
        print(f"\033[31m[-]\033[0m {message}")

# Init logger
Log = Logger()

app = Flask(__name__, static_folder='static')

from app import views