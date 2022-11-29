import os
import json
import flask
import threading

app = flask.Flask(__name__)
app.secret_key = os.environ["FLASK_APP_SECRET"]

cfg = json.load(open("config/server.json"))
app.config.from_mapping(cfg["application"])

thread = threading.Thread(target=app.run, kwargs=cfg["launcher"])

from .filters import *

from .routes.commit import *
from .routes.index import *
from .routes.editor import *

from .processors import *