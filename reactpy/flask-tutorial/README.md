# Documentation in Flask

``` Project Dir
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

## Paths

`flaskr/` a Python package containing your application code and files.
`tests/`,  a directory containing test modules.
`.venv/`, a Python virtual environment where Flask and other dependencies are installed.

## Database

`g` is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.

`current_app` is another special object that points to the Flask application handling the request. Since you used an application factory, there is no application object when writing the rest of your code. `get_db` will be called when the application has been created and is handling a request, so `current_app` can be used.

`sqlite3.connect()` establishes a connection to the file pointed at by the **DATABASE** configuration key. This file doesn’t have to exist yet, and won’t until you initialize the database later.

`sqlite3.Row` tells the connection to return rows that behave like dicts. This allows accessing the columns by name.

`close_db` checks if a connection was created by checking if `g.db` was set. If the connection exists, it is closed. Further down you will tell your application about the `close_db` function in the application factory so that it is called after each request.

## Blue Print and Views

This creates a Blueprint named 'auth'. Like the application object, the blueprint needs to know where it’s defined, so `__name__` is passed as the second argument. The `url_prefix` will be prepended to all the URLs associated with the blueprint.

1. `@bp.route` associates the URL `/register` with the `register` view function. When Flask receives a request to `/auth/register`, it will call the `register` view and use the return value as the response.

2. If the user submitted the form, `request.method` will be **'POST'**. In this case, start validating the input.

3. `request.form` is a special type of `dict` mapping submitted form keys and values. The user will input their username and password.

4. Validate that `username` and `password` are not empty.

5. If validation succeeds, insert the new user data into the database.

   - db.execute takes a SQL query with ? placeholders for any user input, and a tuple of values to replace the placeholders with. The database library will take care of escaping the values so you are not vulnerable to a SQL injection attack.

   - For security, passwords should never be stored in the database directly. Instead, generate_password_hash() is used to securely hash the password, and that hash is stored. Since this query modifies data, db.commit() needs to be called afterwards to save the changes.

   - An sqlite3.IntegrityError will occur if the username already exists, which should be shown to the user as another validation error.

6. After storing the user, they are redirected to the login page. `url_for()` generates the URL for the login view based on its name. This is preferable to writing the URL directly as it allows you to change the URL later without changing all code that links to it. `redirect()` generates a redirect response to the generated URL.

7. If validation fails, the error is shown to the user. `flash()` stores messages that can be retrieved when rendering the template.

8. When the user initially navigates to `auth/register`, or there was a validation error, an HTML page with the registration form should be shown. `render_template()` will render a template containing the HTML, which you’ll write in the next step of the tutorial.

### Logins

1. The user is queried first and stored in a variable for later use.

`fetchone()` returns one row from the query. If the query returned no results, it returns None. Later, `fetchall()` will be used, which returns a list of all results.
2. `check_password_hash()` hashes the submitted password in the same way as the stored hash and securely compares them. If they match, the password is valid.
3. **session** is a `dict` that stores data across requests. When validation succeeds, the user’s id is stored in a new session. The data is stored in a cookie that is sent to the browser, and the browser then sends it back with subsequent requests. Flask securely signs the data so that it can’t be tampered with.

### Logout

To log out, you need to remove the user id from the session. Then load_logged_in_user won’t load a user on subsequent requests.

## Templates

Templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.

In your application, you will use templates to render HTML which will display in the user’s browser. In Flask, Jinja is configured to autoescape any data that is rendered in HTML templates. This means that it’s safe to render user input; any characters they’ve entered that could mess with the HTML, such as `<` and ``>` will be escaped with safe values that look the same in the browser but don’t cause unwanted effects.

Jinja looks and behaves mostly like Python. Special delimiters are used to distinguish Jinja syntax from the static data in the template. Anything between `{{ and }}` is an expression that will be output to the final document. `{% and %}` denotes a control flow statement like `if` and `for`. Unlike Python, blocks are denoted by start and end tags rather than indentation since static text within a block could change indentation.

### Base Layout

There are three blocks defined here that will be overridden in the other templates:

1. `{% block title %}` will change the title displayed in the browser’s tab and window title.

2. `{% block header %}` is similar to title but will change the title displayed on the page.

3. `{% block content %}` is where the content of each page goes, such as the login form or a blog post.

### Register

`{% extends 'base.html' %}` tells Jinja that this template should replace the blocks from the base template. All the rendered content must appear inside `{% block %}` tags that override blocks from the base template.

A useful pattern used here is to place `{% block title %}` inside `{% block header %}`. This will set the title block and then output the value of it into the header block, so that both the window and page share the same title without writing it twice.

The `input` tags are using the `required` attribute here. This tells the browser not to submit the form until those fields are filled in. If the user is using an older browser that doesn’t support that attribute, or if they are using something besides a browser to make requests, you still want to validate the data in the Flask view. It’s important to always fully validate the data on the server, even if the client does some validation as well.
