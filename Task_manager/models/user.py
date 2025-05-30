from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    tasks = relationship("Task", back_populates="user")

    def __repr__(self):
        return f"<User {self.name} ({self.email})>"
