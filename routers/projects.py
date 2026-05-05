from fastapi import Depends
from fastapi import HTTPException, status
from schemas import *
from database import get_db
from sqlalchemy.orm import Session
from DBModels import *
from typing import List
from oauth2 import *

from fastapi import APIRouter
router = APIRouter()
@router.get("/projects", response_model=List[ProjectResponseModel])
def get_project_info(db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    fetched_project_rec = db.query(ProjectsTable).filter(ProjectsTable.user_id==curr_user.token_user_id).all()
    if not fetched_project_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No records to show for this user")
    return fetched_project_rec

@router.post("/projects", response_model=ProjectResponseModel, status_code=status.HTTP_201_CREATED)
def create_project(new_project:Projects, db:Session=Depends(get_db), curr_user:TokenData=Depends(get_current_user)):
    new_rec = ProjectsTable(project_title=new_project.title, user_id=curr_user.token_user_id)
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    return new_rec