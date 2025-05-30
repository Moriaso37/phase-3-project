from database import session
from models.user import User
from models.project import Project
from models.task import Task
from tabulate import tabulate

def main_menu():
    while True:
        print("\n=== Task Manager CLI ===")
        print("1. View Users")
        print("2. View Projects")
        print("3. View Tasks")
        print("4. Add User")
        print("5. Add Project")
        print("6. Add Task")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_users()
        elif choice == '2':
            view_projects()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            add_user()
        elif choice == '5':
            add_project()
        elif choice == '6':
            add_task()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def view_users():
    users = session.query(User).all()
    data = [(u.id, u.name, u.email) for u in users]
    print(tabulate(data, headers=["ID", "Name", "Email"], tablefmt="grid"))

def view_projects():
    projects = session.query(Project).all()
    data = [(p.id, p.name, p.description) for p in projects]
    print(tabulate(data, headers=["ID", "Name", "Description"], tablefmt="grid"))

def view_tasks():
    tasks = session.query(Task).all()
    data = [(t.id, t.title, t.status, t.user.name if t.user else "None", t.project.name if t.project else "None") for t in tasks]
    print(tabulate(data, headers=["ID", "Title", "Status", "Assigned User", "Project"], tablefmt="grid"))

def add_user():
    name = input("Name: ")
    email = input("Email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"User {name} added.")

def add_project():
    name = input("Project Name: ")
    description = input("Description: ")
    project = Project(name=name, description=description)
    session.add(project)
    session.commit()
    print(f"Project {name} added.")

def add_task():
    title = input("Task Title: ")
    status = input("Status (e.g., pending, complete): ")
    user_id = int(input("Assign to User ID: "))
    project_id = int(input("Assign to Project ID: "))
    task = Task(title=title, status=status, user_id=user_id, project_id=project_id)
    session.add(task)
    session.commit()
    print(f"Task {title} added.")
