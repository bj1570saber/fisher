from flask import Flask, make_response
from config import DEBUG
from helper import is_isbn_or_key
app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''
    q(isbn -> q): keyword || isbn ;
    page (start, count):
    '''
    isbn_or_key = is_isbn_or_key(q) # return 'key' or 'isbn'

    pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)


