from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
app = Flask(__name__)

app.config.from_object(Config)

from . import routes
from . import api
bootstrap = Bootstrap(app)
