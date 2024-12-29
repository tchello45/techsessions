# Tech Session 1 - Introduction to Flask - Part 1
## Introduction to Flask and setting up a basic Flask application
>*Attention: Please make sure you have installed Flask in a virtual environment before starting this part. If you haven't installed Flask yet, please refer to the [Installation](../README.md#installation) section in the [Introduction to Flask](../README.md) document.*

>*A quickstart guide to Flask is available at [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/).*
### How to set up a basic Flask application
Folder structure of the project:
```
part1
│   app.py
```
To create a basic Flask application, follow these steps:
1. Create a new directory for the project:
```bash
mkdir part1
cd part1
touch app.py
```

2. Create a new Python file `app.py` and add the following code:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
Explanation of the code:
- `from flask import Flask`: Import the Flask class from the `flask` module.
- `app = Flask(__name__)`: Create an instance of the Flask class with the name of the current module.
- `@app.route('/')`: Define a route for the root URL `/` that calls the `hello_world` function.
- `def hello_world()`: Define the `hello_world` function that returns the string `'Hello, World!'`.
- `if __name__ == '__main__':`: Check if the script is executed directly and run the Flask application in debug mode on `0.0.0.0:5000`.

>*Reminder: The `0.0.0.0` host starts the Flask application on all available network interfaces, and the `5000` port specifies the port number on which the Flask application will run. EVERYONE in the network can access the application. If you want to restrict access to the application, you can use `127.0.0.1` as the host to run the application locally.*

Alternatively, you can run the Flask application using the following command:
```bash
flask --app <name_of_python_file_without_extension> run --host=<host_ip> --port=<port_number>
```
For example:
```bash
flask --app app run --host=0.0.0.0 --port=5000 --debug
``` 

If you open a web browser and navigate to `http://<your ip><your port>/` you should see the message `Hello, World!`.
- The browser renders the message `Hello, World!` as html content.
- You can change the message to any other message or html content.
- If you have a long html content, you can use the `render_template` function to render the html content from a separate html file in the `templates` folder.<br>
Example:
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
...
```
Folder structure of the project:
```
part1
│   app.py
│   templates
│   │   index.html
```
- The `index.html` file contains the html content that you want to render.
- The `render_template` function renders the html content from the `index.html` file.

### Make the page dynamic
You can make the page dynamic by passing variables through the URL. To do this, you can define a route with a variable part that will be passed to the function as an argument.<br>For example:
```python
@app.route('/') # Default route without a variable part
def hello_world():
    return 'Hello, World!'
@app.route('/<name>') # Route with a variable part
def hello_name(name):
    return f'Hello, {name}!'
```
If you navigate to `http://<your ip><your port>/John`, you should see the message `Hello, John!`.<br>
If you navigate to `http://<your ip><your port>/`, you should see the message `Hello, World!`. -> Default route without a variable part.
> *Attention: The variable part of the URL is passed as an argument to the function and gets rendered in the message! If you pass a malicious script, it will be executed in the browser!*

For example if you navigate to `http://<your ip><your port>/<script>alert('Hello, World!')</script>`, you will see an alert message `Hello, World!`.
To prevent this, you can use the `escape` function from the `markupsafe` module to escape the variable part of the URL.
```python
from markupsafe import escape

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {escape(name)}!'
```
If you navigate to `http://<your ip><your port>/<script>alert('Hello, World!')</script>`, you will see the message `Hello, &lt;script&gt;alert('Hello, World!')&lt;/script&gt;`.<br><br>
You can add as many subdirectories as you want to the URL. For example:
```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/user/<username>/<int:post_id>')
def show_post(username, post_id):
    return f'Post {post_id} from user {username}'
```
If you navigate to `http://<your ip><your port>/user/John`, you should see the message `User John`.
If you navigate to `http://<your ip><your port>/user/John/123`, you should see the message `Post 123 from user John`.

### Introduction to Flask templates
Like we saw earlier, we will get to our limit if we want to render a long html content in the function. Now we want to pass a variable to the html content. To do this, we can use the **Jinja2** templating engine.
The folder structure is the same as before:
```
part1
|   app.py
|   templates
|   |   index.html
```
The `index.html` file contains the following content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello, World!</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```
The `{{ name }}` part is a placeholder for the variable `name` that we want to pass to the html content.

To render the html content from the `index.html` file, we can use the `render_template` function from the `flask` module.
```python
@app.route('/<name>')
def hello_name(name):
    return render_template('index.html', name=name)
```
If you navigate to `http://<your ip><your port>/John`, you should see the message `Hello, John!`.<br><br>
The Jinja2 templating engine is a powerful tool that allows you to create dynamic web pages by passing variables to the html content. If you view the source code of the page in the browser, you will see the rendered html content.<br><br>
Browser -> GET request -> Flask -> HTML Template -> Jinja2 rendering -> HTML content -> Browser<br><br>
After the rendering process, the browser renders the html content as a web page and can NOT see the Jinja2 template code.
>*Attention: The Jinja2 template engine uses html escaping by default to prevent XSS attacks.*

If you want to take a deeper look at the Jinja2 templating engine, you can visit the [Jinja2 Documentation](https://jinja.palletsprojects.com/en/stable/) it is really helpful and worth a look. We want to use the Jinja2 templating engine in the next parts of the session to create dynamic web pages.

### Conclusion
In this part, we learned...
- how to set up a basic Flask application,
- how to make the page dynamic by passing variables through the URL,
- how to use the Jinja2 templating engine to render html content from a separate html file.