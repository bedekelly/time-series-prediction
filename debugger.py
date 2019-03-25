import flask
from urllib.parse import unquote
from flask import Flask

app = Flask(__name__)


@app.route("/<expr>/<input_data>")
def debug(expr, input_data):
    e = unquote(expr)
    d = unquote(input_data)
    with open("logs.txt", "a") as f:
        f.write(e + "\n")
        f.write(d + "\n")
    return "thanks v much"


app.run(host="0.0.0.0", port=8000)
