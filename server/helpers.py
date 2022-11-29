import time
import flask
import tempfile


def clear_fn():
    del flask.session["fn"]
    del flask.session["semantic-fn"]


def tmpfile(content=b""):
    now = int(time.time())

    fo = tempfile.NamedTemporaryFile(
        prefix="bdk-",
        delete=False,
        suffix=f"-{now}",
    )

    fo.write(content);
    
    return fo
