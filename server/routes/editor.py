import os
import flask
from server import app
import xml.etree.ElementTree as ET
from ..helpers import clear_fn, tmpfile


@app.route("/editor")
def r_editor():
    if not flask.session.get("fn"):
        return flask.render_template("editor/err/401.html")

    try:
        fh = open(flask.session["fn"])
    except FileNotFoundError:
        clear_fn()
        return flask.render_template("editor/err/410.html")

    try:
        ET.ElementTree(ET.fromstring(str(fh.read())))
    except ET.ParseError as e:
        clear_fn()
        return flask.render_template("editor/err/400.html", err=str(e))
    
    return flask.stream_template("editor/editor.html")


@app.route("/editor/download")
def r_editor_download():
    return flask.send_file(
        flask.session["fn"],
        as_attachment=True,
        download_name=flask.session["semantic-fn"]
    )


@app.route("/editor/preset")
def r_editor_preset():
    name = flask.request.args.get("name")
    fns = next(os.walk("server/static/presets/"), (None, None, []))[2]
    fns = [file.replace(".xml", "") for file in fns]
    path = f"server/static/presets/{name}.xml"

    if name not in fns:
        return flask.abort(404)

    with open(path, "r") as fh:
        fo = tmpfile(content=fh.read().encode("UTF-8"))
        flask.session["fn"] = path
        flask.session["semantic-fn"] = fh.name

    return flask.redirect("/editor?s=preset")


@app.route("/editor/create", methods=["POST"])
def r_editor_create():
    fh = flask.request.files["save"]
    fo = tmpfile(content=fh.read())
    flask.session["fn"] = fo.name
    flask.session["semantic-fn"] = fh.filename

    return flask.redirect("/editor?s=upload")
