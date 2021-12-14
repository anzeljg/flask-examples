"""

This is a simple URL shortener web application.

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
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import HTTPException

# Import Flask WTForms modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Import Flask SQLAlchemy modules
from flask_sqlalchemy import SQLAlchemy

# Import other modules
from hashlib import sha512


# ========== Create application ========== #

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


# ========== Utility functions ========== #
# See: https://medium.com/@ivan.georgiev_19530/generate-short-url-from-string-in-python-ac94e1e957ae

def int2encoding(number, encoding_table):
    """
    Encode integer into string, using digit encoding table.
    
    You can encode integer into hexadecimal string (16 digit table):
    
    >>> int2encoding(20190925, table16)
    '13416cd'
    
    To verify use, python's hex() function:
    
    >>> hex(20190925)
    '0x13416cd'
    
    You can encode integer using 64 digit table:
    
    >>> int2encoding(20190925, table64)
    '1d1rd'
    """

    if number == 0:
        return encoding_table[0]
    
    base = len(encoding_table)
    digits = ''
    while number:
        digits += encoding_table[int(number % base)]
        number //= base
    return digits[::-1]


def short_str(value, length=6, encoding_type=64):
    """
    Geneate string hash with given length, using specified encoding table.
    
    Generating hash with length of 8 characters, using hexadecimal encoding table:
    
    >>> short_str("hello world", 8, 16)
    '309ecc48'
    
    Generating hash with length of 8 charactes, using extended 64-digit encoding table:
    
    >>> short_str("hello world", 8, 64)
    'MDIN8D1b'
    """
    
    if length > 128:
        raise ValueError('Length exceeds 128 characters.')

    if encoding_type == 64:
        table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
    else:
        table = '0123456789abcdef'
    
    hash = sha512(value).hexdigest()
    encoded_hash = int2encoding(int(hash, 16), table)
    return encoded_hash[0:length]


# ========== Route definitions ========== #
#
#  HTTP method | URL path         | Controller function
# -------------+------------------+----------------------
#  GET, POST   | /                | link_create()
#  GET         | /<short>         | link_redirect(short) 
# -------------+------------------+----------------------
#

# Index page for URL shortening application
@app.route('/', methods=['GET', 'POST'])
def link_create():
    # Setup form
    form = LinkForm()

    # Process form
    if form.validate_on_submit():
        # Handle adding or updating data to the database
        if request.method == 'POST' and 'submit' in request.form:

            short = short_str(form.long.data.encode('utf-8'))
            record = db.session.query(Link).get(short)

            # Update record if it exists in the database
            if record:
                record.short = short
                record.long  = request.form.get('long')
                record.hits += 1
            # Create new record
            else:
                record = Link(
                    short = short,
                    long  = request.form.get('long'),
                    hits  = 0
                )

            # Save record details to the database
            db.session.merge(record)
            db.session.commit()
            
            # Add full version of shortened URL, e.g. http://127.0.0.1:5000/aBcDeF
            record.short_url = request.url_root + record.short

            return render_template('link.html', link=record)

    return render_template('index.html', form=form)


# Reroute/redirect existing short link
@app.route('/<short>', methods=['GET'])
def link_redirect(short):
    # Get a given existing short link
    record = db.session.query(Link).get(short)

    # Redirect, if short link exists
    if record:
        # Update record hit counter
        record.hits += 1
        db.session.commit()
        # Redirect to original full URL
        return redirect(record.long)
    else:
        error = 'Shortened URL address not found in the database!'
        return render_template('error.html', error=error)


# Handle HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(error):
    return render_template('error.html', error=error), error.code


# ========== Form definitions ========== #

# Form to add/update URL link to be shortened
class LinkForm(FlaskForm):
    long = StringField(
        'URL Address',
        validators=[DataRequired('You must provide a valid URL address!')]
    )
    submit = SubmitField('Shorten')


# ========== Database model definitions ========== #

# Database model for Link entity
class Link(db.Model):
    __tablename__ = 'link'
    short = db.Column(db.String, nullable=False, primary_key=True, unique=True)
    long  = db.Column(db.String, nullable=False)
    hits  = db.Column(db.Integer, default=0)

    def __init__(self, short, long, hits):
        self.short = short
        self.long  = long
        self.hits  = hits

    def __repr__(self):
        return '<Link %r>' % self.short


# ========== Create database ========== #

with app.app_context():
    # Create the database/tables if it/they don't exist yet
    # This call has to be after database model definitions!
    db.create_all()


# ========== Run application ========== #

if __name__ == '__main__':
    # Run application and development server
    app.run(debug=True)
