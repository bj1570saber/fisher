from flask import Flask, make_response
from config import DEBUG

app = Flask(__name__)

@app.route('/new')
def new():
    return 'new'

@app.route('/hello-404') # http://0.0.0.0:5000/hello-404
def hello_404():

    # 404: meaning: Not found page, but It does not affect display content,
    # if content is not empty.
    headers = {
        'content-type': 'text/plain'
    }
    response = make_response('<html><body><h1>love</h1></body></html>', 404)
    response.headers = headers
    return response # display: <html><body><h1>love</h1></body></html>

@app.route('/hello-301') # http://0.0.0.0:5000/hello-301
def hello_301():
    # 301:redirect to specific 'location' in headers. Content body will not display.
    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    
    response = make_response('<html><body><h1>love</h1></body></html>', 301)
    response.headers = headers
    return response

@app.route('/hello-json')  # http://0.0.0.0:5000/hello-json
def hello_json(): # return app api:
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }

    response = make_response('<html><body><h1>love</h1></body></html>', 404)
    response.headers = headers
    return response

# Most popular way to return:
@app.route('/hello-short_return')  # http://0.0.0.0:5000/hello-short_return
def hello_short_return():
    headers = {
        'content-type': 'application/json',
        'location': 'http://www.bing.com'
    }
    return '<html></html>', 200, headers # code 200 will not invoke redirection 'location'
    # this return is returning a tuple. Flask will convert to a response object.
'''
 also return other info:
 status code 200, 404, 301...
 content-type http headers, default: text/html
'''

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)


