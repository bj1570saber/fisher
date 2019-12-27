from flask import jsonify
from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook

print('book_1: ', id(app))


@app.route('/book/search/<q>/<page>')
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
