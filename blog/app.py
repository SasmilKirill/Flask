from datetime import time

from flask import Flask, g
from flask import request

app = Flask(__name__)


@app.route('/<int:x>/<int:y>', methods=['GET', 'POST'])
def index(x: int, y: int,):
    return f'Hello, {x ** y}!'

@app.before_request
def process_before_request():
    """
    Sets start_time to `g` object
    """

    g.start_time = time()


@app.after_request
def process_after_request(response):
    """
    adds process time in headers
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time

    return response


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error):
    return '404'
