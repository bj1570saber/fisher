from httper import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @staticmethod
    def search_by_isbn(isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HTTP.get(url)  # return format: Json by default parameter
        #  dict
        return result

    @staticmethod
    def search_by_keyword(keyword, count=15, start=0):
        url = YuShuBook.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
