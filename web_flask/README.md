# Project Title: Airbnb Clone with Flask

## Overview

This project aims to create a full-stack Airbnb clone using Flask, a lightweight and flexible Python web framework. Flask provides the necessary tools and libraries to build web applications efficiently, offering features for routing, template rendering, and interacting with databases like MySQL. This README.md serves as a guide to understanding Flask and implementing various functionalities within the project.

- Everything is rendered from a template fetching database data, from filter drop downs to reviews!
  
![image](https://github.com/LWSSIM/AirBnB_clone_v2/assets/127129101/d48f5d46-3650-489c-984c-e9653a5a6fb8)


### What is a Web Framework?

A web framework is a collection of libraries, tools, and conventions that simplifies the process of building web applications. It provides developers with a structured way to handle tasks such as routing URLs, rendering templates, managing sessions, and interacting with databases.

### How to Build a Web Framework with Flask

Flask allows developers to create web applications in Python with minimal boilerplate code. To start building a web framework with Flask, follow these steps:

1. Install Flask using pip:
   
   ```bash
   pip install Flask
   ```

2. Create a Python file (e.g., `app.py`) to define your Flask application.

3. Import Flask and create an instance of the Flask class:

   ```python
   from flask import Flask
   app = Flask(__name__)
   ```

4. Define routes and their respective view functions to handle incoming requests.

5. Run the Flask development server:

   ```bash
   flask run
   ```

### How to Define Routes in Flask

Routes in Flask are defined using the `@app.route()` decorator. A route maps a URL pattern to a view function, which generates an HTTP response for that URL.

```python
@app.route('/')
def index():
    return 'Welcome to the homepage'
```

### What is a Route?

A route in Flask defines a mapping between a URL and a view function. When a client sends a request to a specific URL, Flask invokes the corresponding view function to generate an HTTP response.

### How to Handle Variables in a Route

Variables can be included in routes by specifying `<variable_name>` within the URL pattern. These variables can then be accessed within the corresponding view function.

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'
```

### What is a Template?

A template in Flask is an HTML file that contains placeholders for dynamic content. Templates allow developers to separate the presentation layer from the application logic, making it easier to maintain and modify the user interface.

### How to Create an HTML Response in Flask by Using a Template

Flask uses the Jinja2 template engine to render HTML templates. Templates are stored in the `templates` directory by default. To render a template, use the `render_template()` function provided by Flask.

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

### How to Create a Dynamic Template (Loops, Conditions...)

Jinja2 templates support various control structures such as loops, conditions, and filters. This allows for dynamic content generation based on the data passed from the view function.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User List</title>
</head>
<body>
    <ul>
        {% for user in users %}
        <li>{{ user }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### How to Display in HTML Data from a MySQL Database

To display data from a MySQL database in HTML, first, establish a connection to the database using a library like `mysql-connector-python`. Then, execute SQL queries to retrieve the desired data and pass it to the template for rendering.

```python
import mysql.connector
from flask import render_template

@app.route('/users')
def users():
    conn = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="dbname"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    users = [row[0] for row in cursor.fetchall()]
    conn.close()
    return render_template('users.html', users=users)
```

This README provides a basic understanding of Flask and outlines how to implement key features such as routing, template rendering, and database interaction within the Airbnb clone project. Feel free to explore Flask's documentation for more advanced functionalities and best practices.
