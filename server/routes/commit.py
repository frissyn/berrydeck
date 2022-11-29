import flask
import traceback
from server import app
from server.pipeline import Pipeline


RES = {
    "BAD": (
        "Changes could not be commited to the savefile, " +
        "try again momentarily. [<b>Error:</b> <i>{0}</i>]"
    ),
    "OK": (
        "Changes commited to the savefile successfully. " + 
        "Click '<b>Download Savefile</b>' to save edited file."
    )
}


@app.route("/commit/<string:name>", methods=["POST"])
def r_commit_wildcard(name: str):
    values = dict(flask.request.get_json(force=True))

    try:
        getattr(Pipeline, name)(values)
    except Exception as e:
        traceback.print_exc()
        return RES["BAD"].format(e), 500
    else:
        return RES["OK"], 200
