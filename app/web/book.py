print(__name__)

from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web
# print('book_1: ', id(app)) # for debug
# blueprint -> resolve cyclical import



@web.route('/book/search/<q>/<page>')  # http://0.0.0.0:5000/book/search/9787501524044/1
def search(q, page):
    """
    q(isbn -> q): keyword || isbn ;
    page (start, count):
    """
    isbn_or_key = is_isbn_or_key(q)  # return 'key' or 'isbn'
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)  # return dict type
    else:
        result = YuShuBook.search_by_keyword(q)  # return dict type
    #  return json.dumps(result), 200, {'content-type':'application/json'}
    return jsonify(result)  # flask-jsonify()
