from fastapi import Depends
from fastapi import HTTPException, status
from .. import schemas
from .. database import get_db
from sqlalchemy.orm import Session
from .. import DBModels
from typing import List
from .. import utils

from fastapi import APIRouter
router = APIRouter()

@router.post("/users", response_model=schemas.UsersResponseModel, status_code=status.HTTP_201_CREATED)
def sign_up_user(new_user:schemas.Users, db:Session=Depends(get_db)):
    new_rec = DBModels.UsersTable(user_email=new_user.email, password=utils.convert_password_to_hash(new_user.password))
    db.add(new_rec)
    db.commit()
    db.refresh(new_rec)
    return new_rec

@router.get("/users", response_model=List[schemas.UsersResponseModel])
def users_info(db:Session=Depends(get_db)):
    fetched_user_record = db.query(DBModels.UsersTable).all()
    if not fetched_user_record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No records at the moment!")
    return fetched_user_record

@router.get("/users/{user_id}", response_model=schemas.UsersResponseModel)
def get_user_by_ID(user_id:int, db:Session=Depends(get_db)):
    fetched_rec = db.query(DBModels.UsersTable).filter(DBModels.UsersTable.user_id == user_id).first()
    if not fetched_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user found")
    return fetched_rec

