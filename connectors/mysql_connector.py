from sqlalchemy import create_engine
import os

# MySQL Connector using SQLAlchemy Engine
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database_name = os.getenv("DB_NAME")

# Print the connection string to connect to the database
print("Connecting to SQL database")

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}'
engine = create_engine(connection_string)

# Connect to the database
connection = engine.connect()

# Print the connection object to check if it's connected to the database
print("Success Connecting to SQL database")