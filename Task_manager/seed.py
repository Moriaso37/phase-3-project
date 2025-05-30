from database import Base, engine, session
from models.user import User
from models.project import Project
from models.task import Task

# Drop and recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Sample data
u1 = User(name="Alice", email="alice@example.com")
u2 = User(name="Bob", email="bob@example.com")

p1 = Project(name="Website Redesign", description="Revamp the company website")
p2 = Project(name="Marketing Campaign", description="Social media ads")

t1 = Task(title="Create wireframes", status="pending", user=u1, project=p1)
t2 = Task(title="Write blog post", status="complete", user=u2, project=p2)

session.add_all([u1, u2, p1, p2, t1, t2])
session.commit()

print("Database seeded!")
