from flask import Flask, make_response
from config import DEBUG

app = Flask(__name__)

@app.route('/hello')
def hello():
    # 404:
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html><body><h1>love</h1></body></html>', 404)
    # 404: Not found page, but will display anyway.

    # 301:
    '''
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    
    response = make_response('<html><body><h1>love</h1></body></html>', 301)
    # 301:redirect to specific 'location' in headers. Content body will not display.
    # Another way to return:
    #return '<html></html>', 301, headers
    '''
    # return app api:
    '''
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    '''    '''
    response = make_response('<html><body><h1>love</h1></body></html>', 404)
    '''
    # response.headers = headers
    # return response
'''
 also return other info:
 status code 200, 404, 301...
 content-type http headers, default: text/html
 '''


def greeting():
    return 'Welcome to greeting page.'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)


