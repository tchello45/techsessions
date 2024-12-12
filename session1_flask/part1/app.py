from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__) # app is an instance of the Flask class

@app.route('/hello_world') # We can now access this function by going to http://<ip>:<port>/hello_world/
def hello_world():
    return 'Hello, World!'

@app.route('/') # We can return html content as well
def home():
    return '<h1>Welcome to the home page</h1><p>This is a paragraph</p>'

@app.route('/template') # And use templates if the html content is too long / complex
def template():
    return render_template('template.html') # The template.html file should be in the templates folder

@app.route('/user/<name>') # We can also pass parameters to the function to asure dynamic content
def user(name):
    return f'Hello, {escape(name)}!' # We can use the escape function to prevent XSS attacks

@app.route('/template/<name>') # We can use the Jinja2 templating engine to pass parameters to the template
def template_user(name):
    return render_template('template_user.html', name=name) # Another template file in the templates folder with jinja2 syntax



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)