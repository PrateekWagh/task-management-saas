from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from database import Base

# New users registration/signup table
class UsersTable(Base):
    __tablename__ = "users_record"
    user_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    projects = relationship("ProjectsTable")


# New Project for different users:
class ProjectsTable(Base):
    __tablename__ = "project_records"
    project_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    project_title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users_record.user_id", ondelete='CASCADE') , nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    owner = relationship("UsersTable")
    tasks = relationship("TasksTable")

# For every project there would be several tasks, therefore tasksTable
class TasksTable(Base):
    __tablename__ = "task_records"
    task_id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    task_title = Column(String, nullable=False)
    task_status = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("project_records.project_id", ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    of_project = relationship("ProjectsTable")