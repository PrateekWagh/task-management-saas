from fastapi import Depends
from fastapi import HTTPException, status
from .. import schemas
from .. database import get_db
from sqlalchemy.orm import Session
from .. import DBModels
from typing import List
from .. import oauth2

from fastapi import APIRouter
router = APIRouter()
@router.get("/projects", response_model=List[schemas.ProjectResponseModel])
def get_project_info(db:Session=Depends(get_db), curr_user:schemas.TokenData=Depends(oauth2.get_current_user)):
    fetched_project_rec = db.query(DBModels.ProjectsTable).filter(DBModels.ProjectsTable.user_id==curr_user.token_user_id).all()
    if not fetched_project_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No records to show for this user")
    return fetched_project_rec

@router.post("/projects", response_model=schemas.ProjectResponseModel, status_code=status.HTTP_201_CREATED)
def create_project(new_project:schemas.Projects, db:Session=Depends(get_db), curr_user:schemas.TokenData=Depends(oauth2.get_current_user)):
    new_rec = DBModels.ProjectsTable(project_title=new_project.title, user_id=curr_user.token_user_id)
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    return new_rec