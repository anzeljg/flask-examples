# Flask through examples

[Flask](http://flask.pocoo.org) is a small framework by most standards—small enough to be called a "microframework" and small enough that once you become familiar with it, you will likely be able to read and understand all of its source code.

But being small does not mean that it does less than other frameworks. Flask was designed as an extensible framework from the ground up; it provides a solid core with the basic services, while extensions provide the rest. Because you can pick and choose the extension packages that you want, you end up with a lean stack that has no bloat and does exactly what you need.

Flask has three main dependencies. The routing, debugging, and Web Server Gateway Interface (WSGI) subsystems come from [Werkzeug](http://werkzeug.pocoo.org); the template support is provided by [Jinja2](http://jinja.pocoo.org); and the command-line integration comes from [Click](http://click.pocoo.org). These dependencies are all authored by Armin Ronacher, the author of Flask.

Flask has no native support for accessing databases, validating web forms, authenticating users, or other high-level tasks. These and many other key services most web applications need are available through extensions that integrate with the core packages. As a developer, you have the power to pick the extensions that work best for your project, or even write your own if you feel inclined to. This is in contrast with a larger framework, where most choices have been made for you and are hard or sometimes impossible to change.

In all example project in this repository we will use Flask-SQLAlchemy extension to integrate Flask and [SQLAlchemy](https://www.sqlalchemy.org/) for accessing databases and Flask-WTForms extension to integrate Flask and [WTForms](http://wtforms.readthedocs.io/) for everything related to web forms.

There are a lot of very good books and other resources that can help when learning Flask. The one that was particulary helpful for me is [Flask Web Development](https://www.oreilly.com/library/view/flask-web-development/9781491991725/), written by Miguel Grinberg.

## Installation of Flask and extensions

The detailed process of installing Flask and needed extensions for running examples in this repository is described in this [Installation guide](INSTALL.md). Follow this guide closely to successfully install Flask and needed extension before trying out the examples.

## Structuring and executing examples

The project structure of examples in this repository and how to execute/run each project is described in this [Structure and execution guide](EXECUTE.md). Consult this guide to run these examples.

## Recommended order of examples

Although you can run any example after you have successfully installed Flask, it might be good to follow the recommended order. This will guide you from simpler examples to more complex ones. Most examples come in several versions where higher version typically builds on or expands concepts from lower version.

The examples also contain sketches and/or diagrams of the user interface as well as the database (where appropriate).

### Hello World

The idea of this example is that we get to know how to run the built-in server and how MVC (model-view-controller) pattern works. We get to know how to use forms and how to work with form to get the input from the user.

The first version contains only raw HTML code as a response to HTTP requests.

In the second version we get to know how templates work and also make this example look pretty.

- [Hello v.1](/hello_v1/)
- [Hello v.2](/hello_v2/)

### URL Shortener

The idea of this example is to build a working URL shortener (like [Bit.ly](https://bitly.com/)). By this point we are already familiar with Flask, templates and froms. We get to know how to use and work with the database. We will be using SQLite in all of our examples, but it is relatively easy to replace this with another database engine. 

- [Links v.1](/links_v1/)

### Todo List

The idea of this example is to build a working Todo list web application. By this point we are already familiar with Flask, templates, froms and database. We get to know how to use AJAX calls and DOM manipulation to change part of the content of the webpage without reloading the whole thing.

- [Todo v.1](/todo_v1/)

### Personal Blog

The idea of this example is to build a fully functional personal blog, using all knowledge acquired so far. Also we get to know how to include external fonts (e.g. Google Fonts) to display content using non default typography.

In the first version we will add all the blogging features that will allow us to display list of blog posts, display single blog post, add a new blog post, edit an existing blog post and delete an existing blog post.

In the second version we will add user management to our blogging web application, which means the ability to sign in and out of the web application, the ability for users to change their passwords and the ability for administrator to add, edit or delete any user.

In the third version (which does not exist yet) we could expand our blogging web application to allow uploading a photo with any blog post and adding a blog post to a predifined category. Categories could be added, edited and deleted as well. 

- Blog v.1
- Blog v.2
- Blog v.3

### Master Chéf

The idea of this example builds on all previous eamples and synthesize the concepts from all of them to create a complex web application that serves as a recipe book.

In the first version we will build a recipe book that will allow displaying all recipes as well displaying recipes that belong to customizable categories. It will also allow adding, editing, deleting and viewing single recipe. Visitors will be able to see photo of the dish and the entire recipe (that is ingredients, preparation instruction, preparation time, difficulty etc.), they will be able to like or unlike any recipe.

In the second version we will add user management to our web application, which means the ability to sign in and out of the web application, the ability for users to change their passwords and the ability for administrator to add, edit or delete any user.

- Chef v.1
- Chef v.2
