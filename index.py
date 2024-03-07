from flask import Flask
from connectors.mysql_connector import connection

app = Flask(__name__)

# Define the route for the root URL of the website
@app.route('/')
def hello_world():
    return 'Hello, World!'