import json

from flask import Flask
from config import DEBUG
from app.web import book

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, port=5000)
