"""

This is a simple Hello web application that greets the user.

The aim of this web application is to show how to use Flask
framework to start the web server, do simple web page routing
and web page error handling.

Bootstrap framework is used for the formatting of this web
application. This example also shows how to use templates to
format generated web pages.

@author     Gregor Anželj <gregor.anzelj@gmail.com>
@license    GNU GPL
@copyright  (C) Gregor Anželj 2020

"""

# Import Flask modules
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.exceptions import HTTPException

# Import Flask WTForms modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# ========== Create application ========== #

# Create a new instance of flask web application
app = Flask(__name__)
# Flask WTForms needs this against CSRF attacks
app.config['SECRET_KEY'] = 'A really long string that people will not guess'


# ========== Route definitions ========== #
#
#  HTTP method | URL path         | Controller function
# -------------+------------------+----------------------
#  GET         | /                | index()
#  GET         | /greet/<name>    | greet_user(name)
#  GET, POST   | /greeting        | greeting_form()
# -------------+------------------+----------------------
#

# Handle index page
# e.g.: http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template('greet.html', name='Kitty')


# Handle user greeting page
# e.g.: http://127.0.0.1:5000/greet/John
@app.route('/greet/<name>')
def greet_user(name):
    return render_template('greet.html', name=name)


# Handle greeting form page
# e.g.: http://127.0.0.1:5000/greeting
@app.route('/greeting', methods=['GET', 'POST'])
def greeting_form():
    # Setup form
    form = GreetingForm()

    # Process form before populating it with default values
    if form.validate_on_submit():
        # Handle data from the form
        if request.method == 'POST':
            entered_name = form.name.data
            return redirect(url_for('greet_user', name=entered_name))

    return render_template('form.html', form=form)


# Handle HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(error):
    return render_template('error.html', error=error), error.code


# ========== Form definitions ========== #

# Form for user to enter their name
class GreetingForm(FlaskForm):
    name = StringField(
        'Enter name',
        validators=[DataRequired('Person must have a name!')]
    )
    submit = SubmitField('Greet!')


# ========== Run application ========== #

# Run the web server
if __name__ == '__main__':
    app.run()
