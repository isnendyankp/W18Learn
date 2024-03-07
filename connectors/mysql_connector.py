from sqlalchemy import create_engine

# MySQL Connector using SQLAlchemy Engine
username = "root"
password = ""
host = "127.0.0.1"
database_name = "product_review"

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database_name}'
engine = create_engine(connection_string)

