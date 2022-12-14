import re
import flask
from server import app


@app.template_filter('title')
def f_title(s):
    return " ".join(re.findall('[A-Z][^A-Z]*', s))


@app.template_filter('boolean')
def f_boolean(s):
    return "true" if (str(s).lower() == "true") or (str(s).lower() == "on") else "false"


@app.template_filter('check')
def f_check(s):
    return "checked" if (str(s).lower() == "true") or (str(s).lower() == "on") else ""
