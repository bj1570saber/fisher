from flask import Flask
from config import DEBUG

app = Flask(__name__) # default project name
'''
app.config.from_object('config')
print(app.config['DEBUG'])#This key must be all upper-case letters, otherwise, error throw.
#if config.py module does not contain DEBUG constant, this print statement will print 'False',
#  because Flask has a default constant name Debug = False
# This is another way to import config
'''

        #'/hello/' is ok, but not good for SEO, /hello => redirect to ~/hello/
@app.route('/hello') # unique url, better for SEO
# A file has multiple url will be mark as cheating search engine.
# That's why unique url is important. Flask will redirect the correct url
def hello(): # simple view function: http://127.0.0.1:5000/hello
    return 'Hello, visitor. with debug mode'

# another way to direct a page: app.add_url_rule()
def greeting():
    return 'Welcome to greeting page.'

app.add_url_rule('/greeting', view_func=greeting)
# http://127.0.0.1:5000/greeting

# entry .py file must have this if control. It makes sure following code only execute in entrance file.
if __name__ == '__main__': # when file was import, __name__ will be changed
    #When this file was import to other files. following code will not execute.
    # Following code only run in development environment(Flask build-in server - poor performance).
    app.run(host = '0.0.0.0', debug = DEBUG, port = 5000)#app.run invoke Flask build-in server.
    # production environment nginx + uwsgi.
'''
#Another way to import config, config is a sub class of dict
app.run(host = '0.0.0.0', debug = app.config['DEBUG'], port = 5000)
'''


