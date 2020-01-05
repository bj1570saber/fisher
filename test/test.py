# @author: saber1570

from flask import Flask, current_app, request, Request

app = Flask(__name__)
a = current_app  # LocalProxy
d = current_app.config['DEBUG']

