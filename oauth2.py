from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime as dt, timedelta
from schemas import *
import config
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# ----------------------Three components require for creating Token-------------------------------
SECRET_CODE = config.SECRET_CODE
ALGORITHM = config.ALGORITHM
EXPIRATION_TIME = 30

def get_access_token(data:dict):
    to_encode = data.copy()
    expire_time = dt.now()+timedelta(minutes=EXPIRATION_TIME)
    to_encode.update({"exp":expire_time})
    token = jwt.encode(to_encode, SECRET_CODE, ALGORITHM)
    return token

def verify_access_token(token:str, credential_exceptions):
    try:

        payload = jwt.decode(token, SECRET_CODE, ALGORITHM)
        user_id = payload.get("user_id")
        if not user_id:
            raise credential_exceptions
        token_data = TokenData(token_user_id=user_id)
        return token_data
    except JWTError:
        raise credential_exceptions
def get_current_user(token:str=Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Request Not Allowed",
                                         headers={"www-Authenticate":"Bearer"})
    return verify_access_token(token, credential_exception)