import flask
from server import app


@app.template_filter('boolean')
def f_boolean(s):
    return "true" if (s.lower() == "true") or (s.lower() == "on") else "false"


@app.template_filter('check')
def f_check(s):
    return "checked" if (s.lower() == "true") or (s.lower() == "on") else ""
