from fastapi import FastAPI
from database import engine
from DBModels import Base
from routers import users, projects, tasks, auth




Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(auth.router)