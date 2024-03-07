from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection

from sqlalchemy import text
from models.product import Product
from sqlalchemy.orm import sessionmaker

# Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Define the route for the root URL of the website
@app.route('/')
def hello_world():

    # # insert Using SQL
    # Session = sessionmaker(connection)
    # with Session() as s:
    #     s.execute(text("INSERT INTO product (name, price, description, created_at) VALUES ('Steel Wallet', 145000, 'Created from cow skin')"))
    #     s.commit()

    # insert Using Model
    NewProduct = Product( name='Plastic Wallet', price=12000, description='Made from recyled plastic bags', created_at='2021-10-10' )
    Session = sessionmaker(connection)
    with Session() as s:
        s.add(NewProduct)
        s.commit()


    return 'Hello, World!'