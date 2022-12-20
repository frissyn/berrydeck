import re
import flask
import celeste
from server import app


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
            return dict(save=celeste.Savefile.read(flask.session["fn"]))
        except Exception:
            return dict(save=None)

    return dict(save=None)
