import flask
from server import app


@app.route("/")
def r_index():
    return flask.render_template("index.html")


@app.route("/theme")
def r_theme():
    return flask.render_template("theme.html")


@app.route("/credits")
def r_credits():
    return flask.render_template("credits.html")
