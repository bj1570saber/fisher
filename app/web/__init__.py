from flask import Blueprint

web = Blueprint('web', __name__)
print('__name__: ', __name__) #  ???

from app.web import book
from app.web import user