

def is_isbn_or_key(word):
    '''
    test word parameter is a key or isbn
    return 'key' if it's not isbn format, otherwise return 'isbn'.
    '''
    # isbn13: 13 digits
    # isbn10: 10 digits & -
    isbn_or_key = 'key'

    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key