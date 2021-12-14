"""

This is a basic Hello web application that greets the user.

The aim of this web application is to show how to use Flask
framework to start the web server, do simple web page routing
and web page error handling. 

There is no formatting (no CSS) since this is only basic HTML.

@author     Gregor Anželj <gregor.anzelj@gmail.com>
@license    GNU GPL
@copyright  (C) Gregor Anželj 2020

"""

import flask


# Create a new instance of flask web application.
app = flask.Flask(__name__)


# Handle index page
# e.g.: http://127.0.0.1:5000/
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# Handle user greeting page
# e.g.: http://127.0.0.1:5000/John
@app.route('/<name>')
def greet_user(name):
    return '<h1>Hello ' + name + '!</h1>'


# Handle 404 Not Found errors
@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Page not found.</h1><p>We could not locate the page you were searching for ...</p>', 404


# Handle 500 Internal Server errors
@app.errorhandler(500)
def internal_server_error(error):
    return '<h1>Internal server error</h1><p>There is a problem with our server. We are working on that!</p>', 500


# Run the web server
if __name__ == '__main__':
    app.run()
