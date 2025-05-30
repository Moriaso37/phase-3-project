from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))

    user = relationship("User", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task {self.title} [{self.status}]>"
