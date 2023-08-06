from flask import Flask
import platform

app = Flask(__name__)


@app.route('/')
def hello_world():
    version = platform.python_version()
    return '<code>Hello, New World!<br>We\'re using Python ' + version + '</code>'
