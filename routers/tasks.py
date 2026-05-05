from fastapi import Depends
from fastapi import HTTPException, status
from schemas import *
from database import get_db
from sqlalchemy.orm import Session
from DBModels import *
from typing import List

from fastapi import APIRouter
from oauth2 import get_current_user
router = APIRouter()
@router.get("/tasks", response_model=List[TaskResponseModel])
def get_task_info(db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    fetch_curr_user_task_rec = (
    db.query(TasksTable)
    .join(ProjectsTable, TasksTable.project_id == ProjectsTable.project_id)
    .filter(ProjectsTable.user_id == curr_user.token_user_id)
    .all()
    )
    if not fetch_curr_user_task_rec:
        return []
    return fetch_curr_user_task_rec

@router.get("/tasks/{taskID}", response_model=TaskResponseModel)
def get_task_by_ID(taskID:int, db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    fetched_rec =  (db.query(TasksTable).filter(TasksTable.task_id == taskID).
                   join(ProjectsTable, ProjectsTable.project_id == TasksTable.project_id).
                   filter(ProjectsTable.user_id == curr_user.token_user_id).first())
    if not fetched_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Task ID!")
    return fetched_rec

@router.post("/tasks", response_model=TaskResponseModel)
def create_task(user_task_input:Tasks, db:Session=Depends(get_db), current_user:TokenData=Depends(get_current_user)):

    fetch_project_to_use = (db.query(ProjectsTable).filter(ProjectsTable.user_id == current_user.token_user_id).
                            filter(ProjectsTable.project_id==user_task_input.project_id).first())
    if not fetch_project_to_use:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project ID doesn’t exist in DB")

    new_rec = TasksTable(task_title=user_task_input.title, task_status=user_task_input.status,project_id=fetch_project_to_use.project_id)
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    return new_rec


@router.get("/projects/{project_id}/tasks", response_model=List[TaskResponseModel])
def get_tasks_using_project_ID(project_id:int, db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    project_rec = db.query(ProjectsTable).filter(ProjectsTable.project_id==project_id).filter(ProjectsTable.user_id == curr_user.token_user_id).first()
    if not project_rec:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project ID doesn’t exist in DB")
    fetched_rec = (db.query(TasksTable).join(ProjectsTable, TasksTable.project_id == ProjectsTable.project_id)
                   .filter(TasksTable.project_id == project_id).
                   filter(ProjectsTable.user_id == curr_user.token_user_id).all())
    return fetched_rec

@router.put("/tasks/{task_id}", response_model=TaskResponseModel)
def update_task(task_id:int, updated_task_request:TaskUpdateModel, db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    fetched_rec = (db.query(TasksTable).filter(TasksTable.task_id == task_id).
                   join(ProjectsTable, ProjectsTable.project_id == TasksTable.project_id).
                   filter(ProjectsTable.user_id == curr_user.token_user_id).first())
    if not fetched_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task ID doesn’t exist in DB!")

    updated_task_title= updated_task_request.title
    updated_task_status = updated_task_request.status
    if updated_task_title is not None: fetched_rec.task_title = updated_task_title
    if updated_task_status is not None:fetched_rec.task_status=updated_task_status
    db.commit()
    db.refresh(fetched_rec)
    return fetched_rec

@router.delete("/tasks/{task_id}")
def delete_task_by_ID(task_id:int, db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    fetched_rec = (db.query(TasksTable).filter(TasksTable.task_id == task_id).
                   join(ProjectsTable, ProjectsTable.project_id == TasksTable.project_id).
                   filter(ProjectsTable.user_id == curr_user.token_user_id).first())
    if not fetched_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid taskID, request denied!")
    db.delete(fetched_rec)
    db.commit()
    return {"message":"Task deleted successfully!"}