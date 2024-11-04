# models.py
from sqlalchemy import Column, Integer, String, Text
from .database import Base

# Example Model: Item
class MyModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    def __repr__(self):
        return f"<YourModel(name={self.name}, description={self.description})>"
