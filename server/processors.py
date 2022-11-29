import re
import flask
from server import app
import xml.etree.ElementTree as ET
from . import game as celeste


@app.context_processor
def c_sesion_inject():
    return dict(s=flask.session, r=flask.request)


@app.context_processor
def c_game_inject():
    return dict(celeste=celeste, lexicon=celeste.Lexicon)


@app.context_processor
def c_primitive_inject():
    return dict(int=int, str=str, float=float, bytes=bytes)


@app.context_processor
def c_library_inject():
    return dict(re=re)


@app.context_processor
def c_savedata_inject():
    if flask.session.get("fn"):
        try:
            fh = open(flask.session["fn"])
        except FileNotFoundError:
            return dict(save=None)
        else:
            root = ET.fromstring(str(fh.read()))
            tree = ET.ElementTree(root)

            return dict(save=tree)

    return dict(save=None)
