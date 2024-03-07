from sqlalchemy import create_engine

# MySQL Connector using SQLAlchemy Engine
username = "root"
password = ""
host = "127.0.0.1"
database_name = "product_review"

# Print the connection string to connect to the database
print("Connecting to SQL database")

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}'
engine = create_engine(connection_string)

# Connect to the database
connection = engine.connect()

# Print the connection object to check if it's connected to the database
print("Success Connecting to SQL database")