from models.base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

class Product(Base):
    __tablename__ = 'product'
   
#   This is the schema of the product table
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    price = mapped_column(Integer, nullable=False)
    description = mapped_column(String(255), nullable=False)
    created_at  = mapped_column(DateTime, nullable=False)