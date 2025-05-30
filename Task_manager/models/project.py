from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    tasks = relationship("Task", back_populates="project")

    def __repr__(self):
        return f"<Project {self.name}>"
