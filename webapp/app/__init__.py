from flask import Flask
import logging

log = logging.getLogger('werkzeug')
log.disabled = True

app = Flask(__name__, static_folder='static')

from app import views