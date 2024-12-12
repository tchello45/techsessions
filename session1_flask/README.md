# Tech Session - Introduction to Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
## What is Flask?
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies, and several common framework related tools.

## Why Flask?
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

## Features of Flask
- **Development server and debugger**: The development server is a simple but useful server that is included with Flask. It is designed to be used during development and is not suitable for production use. The debugger is a powerful tool that allows you to inspect variables, evaluate expressions, and interact with your application's stack traces.
- **Integrated support for unit testing**: Flask has built-in support for unit testing, which allows you to write tests for your application's functionality. This makes it easy to test your application's behavior and ensure that it works as expected.
- **RESTful request dispatching**: Flask has built-in support for RESTful request dispatching, which allows you to define routes that map to specific HTTP methods. This makes it easy to create APIs that follow RESTful conventions and are easy to understand and use.
- **Jinja2 templating**: Flask uses the Jinja2 templating engine, which allows you to create templates that are rendered into HTML. Jinja2 templates are easy to use and powerful, making it easy to create dynamic web pages.
- **WSGI compliance**: Flask is WSGI compliant, which means that it can run on any WSGI-compliant web server. This makes it easy to deploy Flask applications to a variety of hosting environments.
- **Secure cookies**: Flask has built-in support for secure cookies, which allows you to store session data securely on the client side. This makes it easy to create web applications that require user authentication and authorization.

## Installation
Create a virtual environment and install Flask using pip:
```bash
cd session1_flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Contents
- **Part 1**: Introduction to Flask and setting up a basic Flask application