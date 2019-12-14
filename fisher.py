from flask import Flask
from config import DEBUG

app = Flask(__name__)

@app.route('/hello')
def hello():
    return '<html><body><h1>love</h1></body></html>'
'''
 also return other info:
 status code 200, 404, 301...
 content-type http headers, default: text/html
 
 '''

def greeting():
    return 'Welcome to greeting page.'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)


