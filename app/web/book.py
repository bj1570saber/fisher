from ..forms.book import SearchForm

print(__name__)

from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web


# print('book_1: ', id(app)) # for debug
# blueprint -> resolve cyclical import


@web.route('/book/search')  # http://0.0.0.0:81/book/search?q=9787501524044&page=1
def search():
    """
    q(isbn -> q): keyword || isbn ;
    page (start, count):
    """

    form = SearchForm(request.args)  # request must be called by 'view functions' or it's sub functions;
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data  # form may assign a default value, so it's better than: page = request.args['page']

        isbn_or_key = is_isbn_or_key(q)  # return 'key' or 'isbn'
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)  # return dict type
        else:
            result = YuShuBook.search_by_keyword(q, page)  # return dict type
        #  return json.dumps(result), 200, {'content-type':'application/json'}
        return jsonify(result)  # flask-jsonify()
    else:
        return jsonify(form.errors)


