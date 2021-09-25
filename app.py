from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world, asdfsdaf"


@app.route("/simple-process")
def simple_process_handler():
    first_param = int(request.args.get('x'))
    second_param = int(request.args.get('y'))

    return str(simple_process(first_param, second_param))

def simple_process(first, second, state=""):
    if state == "negate":
        return -1 * (first * second + second)
    return first * second + second