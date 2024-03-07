from flask import Flask

app = Flask(__name__)

# Define the route for the root URL of the website
@app.route('/')
def hello_world():
    return 'Hello, World!'