import json

from flask import Flask
from config import DEBUG


app = Flask(__name__)
print('fishe_1: ', id(app))
from app.web import book

if __name__ == '__main__':
    print('fisher_2: ', id(app))
    app.run(host='0.0.0.0', debug=DEBUG, port=5000)
