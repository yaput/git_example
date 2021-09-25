from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"


@app.route("/simple-process")
def simple_process_handler():
    first_param = int(request.args.get('first'))
    second_param = int(request.args.get('second'))

    return str(simple_process(first_param, second_param))

def simple_process(first, second):
    return first * second + second