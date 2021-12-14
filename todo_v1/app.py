"""
This is a simple TODO list web application.

The aim of this web application is to show how to use Flask
framework to start the web server, do simple web page routing
and web page error handling. The use of database as well as
AJAX request for refreshing parts of the page are also shown.

Bootstrap framework is used for the formatting of this web
application. This example also shows how to use templates to
format generated web pages.

@author     Gregor Anželj <gregor.anzelj@gmail.com>
@license    GNU GPL
@copyright  (C) Gregor Anželj 2020

"""

# Import Flask modules
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.exceptions import HTTPException

# Import Flask WTForms modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Import Flask SQLAlchemy modules
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc


# ========== Create application ========== #

app = Flask(__name__, instance_relative_config=False)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)


# ========== Route definitions ========== #
#
#  HTTP method | URL path          | Controller function
# -------------+-------------------+------------------------
#  GET, POST   | /                 | list_tasks()
#  GET, POST   | /<filter>         | list_tasks()
#  GET, POST   | /task/delete/<id> | delete_task(id)
#  GET         | /task/status/<id> | toggle_task_status(id)
# -------------+-------------------+------------------------
#

# Index page for Todo web application (showing tasks and adding new task)
# For first route to work the 'filter' in the view_tasks() function must
# have default value set, in our case it is set to 'all' to show all tasks
@app.route('/', methods=['GET', 'POST'])
@app.route('/<filter>', methods=['GET', 'POST'])
def list_tasks(filter='all'):

    # If filter is not one of allowed options or filter is empty
    # (which is handled by the default value in function call)
    # then raise '404' or 'Page Not Found' error
    if filter not in ['all', 'active', 'completed']:
        abort(404)

    records = None
    count = 0

    # Get all tasks
    if filter == 'all':
        records = db.session.query(Task)
        count = db.session.query(Task).count()
    # Get active tasks
    if filter == 'active':
        records = db.session.query(Task).filter(Task.complete == 0)
        count = db.session.query(Task).filter(Task.complete == 0).count()
    # Get completed tasks
    if filter == 'completed':
        records = db.session.query(Task).filter(Task.complete == 1)
        count = db.session.query(Task).filter(Task.complete == 1).count()
        
    # Setup form
    form = AddTaskForm()

    # Process form
    if form.validate_on_submit():
        # Handle adding or updating data to the database
        if request.method == 'POST' and 'submit' in request.form:

            # Create new record
            record = Task(
                title = request.form.get('title'),
                complete = 0
            )

            # Save record details to the database
            db.session.merge(record)
            db.session.commit()

    return render_template('index.html', data=records, count=count, filter=filter, form=form)


# Delete existing task
@app.route('/task/delete/<id>', methods=['GET', 'POST'])
def delete_task(id):
    # Get existing task by id
    record = db.session.query(Task).get(id)

    # Setup form
    form = DeleteTaskForm()

    # Process form
    if form.validate_on_submit():
        # Handle deleting task from the database
        if request.method == 'POST' and 'submit' in request.form:

            # Delete task from the database
            db.session.delete(record)
            db.session.commit()
            #flash('Task was successfully deleted.')

        return redirect(url_for('list_tasks'))

    return render_template('delete.html', title='Delete task', form=form)


# Toggle existing task status complete or uncomplete
@app.route('/task/status/<id>/<filter>', methods=['GET', 'POST'])
def toggle_task_status(id, filter='all'):
    # Get existing taks by id
    record = db.session.query(Task).get(id)
    # Toggle/swap/flip complete status
    record.complete = not record.complete

    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        # Status change failed
        return {}

    # Status change successful
    return {'id': id, 'filter': filter}


# Handle HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(error):
    return render_template('error.html', error=error), error.code


# ========== Form definitions ========== #

# Form to add task
class AddTaskForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired('You must provide task title!')]
    )
    submit = SubmitField('Add task')


# Form to delete task
class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')


# ========== Database model definitions ========== #

# Database model for Task entity
class Task(db.Model):
    __tablename__ = 'task'
    id       = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    title    = db.Column(db.String, nullable=False)
    complete = db.Column(db.Boolean, default=0)

    def __init__(self, title, complete=0):
        self.title    = title
        self.complete = complete

    def __repr__(self):
        return '<Task %r>' % self.title


# ========== Create DB with default values ========== #

with app.app_context():
    # Create the database/tables if it/they don't exist yet
    # This call has to be after database model definitions!
    db.create_all()


# ========== Run application ========== #

if __name__ == '__main__':
    # Run application and development server
    app.run(debug=True)
