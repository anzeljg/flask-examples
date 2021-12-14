# Installation guide

Flask supports Python 3.6 and newer, but should be used with the latest version of Python. So before trying to install Flask make sure that you have installed Python version 3.6 or newer.

Python packages are installed with the *pip* package manager, which is included in Python dictribution and installed alongside with Python.

### Installing Flask

To install Flask run the following command:

```
> pip install Flask
```

To show information about installed Flask package run the following command:

```
> pip show Flask
```

This will output:

```
Name: Flask
Version: 1.1.2
Summary: A simple framework for building complex web applications.
Home-page: https://palletsprojects.com/p/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: c:\users\granzelj\appdata\local\programs\python\python38-32\lib\site-packages
Requires: click, Werkzeug, itsdangerous, Jinja2
Required-by:
```

As you can see the information about Flask is displayed which includes the Flask package version, summary, author, license and other information.

The `Requires` line is really important because it lists packages that are required by Flask, so it can run properly. Those packages are:
- `Werkzeug` which implements WSGI, the standard Python interface between applications and servers.
- `Jinja2` which is a template language that renders the pages your application serves.
- `MarkupSafe` which comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
- `ItsDangerous` which securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
- `click` which is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

The `Required-by` line is also really important because it lists packages that require Flask to run properly. Currenlty this line is empty, but later it will contain at least the following packages:
- `Flask-WTForms` which is an extension for Flask that adds support for `WTForms` package that includes CSRF, file upload, and reCAPTCHA.
- `Flask-SQLAlchemy` which is an extension for Flask that adds support for `SQLAlchemy` package that includes methods for accessing and using different database engines like SQLite, MySQL/MariaDB, PostgreSQL and others.

### Installing Flask-WTF

To install Flask-WTF package run the following command:

```
> pip install Flask-WTF
```

To show information about installed Flask-WTF package run the following command:

```
> pip show Flask-WTF
```

This will output:

```
Name: Flask-WTF
Version: 0.14.3
Summary: Simple integration of Flask and WTForms.
Home-page: https://github.com/lepture/flask-wtf
Author: Dan Jacob
Author-email: danjac354@gmail.com
License: BSD
Location: c:\users\granzelj\appdata\local\programs\python\python38-32\lib\site-packages
Requires: itsdangerous, Flask, WTForms
Required-by:
```

As you can see the `Flask-WTF` package also requires `WTForms` package so *pip* will install that too. 

### Installing Flask-SQLAlchemy

To install Flask-SQLAlchemy package run the following command:

```
> pip install Flask-SQLAlchemy
```

To show information about installed Flask-SQLAlchemy package run the following command:

```
> pip show Flask-SQLAlchemy
```

This will output:

```
Name: Flask-SQLAlchemy
Version: 2.4.1
Summary: Adds SQLAlchemy support to your Flask application.
Home-page: https://github.com/pallets/flask-sqlalchemy
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: c:\users\granzelj\appdata\local\programs\python\python38-32\lib\site-packages
Requires: Flask, SQLAlchemy
Required-by:
```

As you can see the `Flask-SQLAlchemy` package also requires `SQLAlchemy` package so *pip* will install that too. 

### Freezing verions of installed packages

When installing Python packages *pip* will always try to install the newest possible version of the package. This might be a problem when developing a web application with one version of the package and then moving code to a server and installing the necessary packages with *pip* and finding out that package version are different which in turn may broke your web application in a worst case scenario.

Luckily *pip* also allows to save package names and versions that we are currently using and later installing the same versions of packages that we were using when we were developing our applications.

To show installed packages and their versions run the following command:

```
> pip freeze
```

This should show installed packages and their versions like:

```
click==7.1.2
Flask==1.1.2
Flask-SQLAlchemy==2.4.1
Flask-WTF==0.14.3
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
SQLAlchemy==1.3.16
Werkzeug==1.0.1
WTForms==2.3.1
```

### Requirements file

Instead of just outputing installed packages and their version it is far more useful to store them in a file. This file could be named almost anything, but by agreement it is usually named `requirements.txt`.

To save installed packages with their version run the following command:

```
> pip freeze > requirements.txt
```

Once you have got your requirements file, you can head over to a different computer or a web server and run the following command:

```
> pip install -r requirements.txt
```

That is assuming you are working in the directory/folder containing the `requirements.txt` file. This tells *pip* to install the specific versions of all the dependencies listed.
