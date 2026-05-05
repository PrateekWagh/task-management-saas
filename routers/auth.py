from fastapi import APIRouter, status, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from DBModels import *
from oauth2 import *
from utils import verify_password



router = APIRouter()
@router.post("/login")
def userLogin(user_log:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    ext_user = db.query(UsersTable).filter(UsersTable.user_email == user_log.username).first()
    if not ext_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No record found")
    if not verify_password(user_log.password, ext_user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token = get_access_token(data={"user_id":ext_user.user_id})
    return {"access_token":f"{access_token}"}