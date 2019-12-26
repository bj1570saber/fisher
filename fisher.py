from flask import Flask, make_response
from config import DEBUG

app = Flask(__name__)

@app.route('/book/search/<q>/<page>')
def search(q,page): # parameters: q(isbn -> q): keyword || isbn ; # page (start, count):
    # isbn13: 13 digits
    # isbn10: 10 digits & -
    isbn_or_key = 'key'

    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'

    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        isbn_or_key = 'isbn'

    pass

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)


