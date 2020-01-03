# @author: saber1570

# sqlalchemy - third party libs
# Flask_SQLQlchemy - a revised version

# WTFORMS
# Flask_WTFORMS
from sqlalchemy import Column, Integer, String

class Book():
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='Unknown')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass