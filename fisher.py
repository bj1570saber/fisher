from flask import Flask

app = Flask(__name__) # default project name
        #'/hello' will be fine
@app.route('/hello/') # redirect；unique url -> better for SEO,
# A file has multiple url will be mark as cheating search engine.
# That's why unique url is important. Flask will redirect the correct url
def hello(): # simple view function: http://127.0.0.1:5000/hello
    return 'Hello, visitor. with debug mode'

# another way to direct a page: app.add_url_rule()
def greeting():
    return 'Welcome to greeting page.'

app.add_url_rule('/greeting', view_func=greeting)
# http://127.0.0.1:5000/greeting

app.run(debug = True)

