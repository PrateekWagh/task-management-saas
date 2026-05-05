from datetime import datetime
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class Users(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UsersResponseModel(BaseModel):
    user_id:int
    user_email:str
    created_at:datetime
    class Config:
        orm_mode = True

class Projects(BaseModel):
    title:str

class ProjectResponseModel(BaseModel):
    project_id:int
    project_title:str
    created_at:datetime
    user_id:int
    owner:UsersResponseModel
    class Config:
        orm_mode = True

class Tasks(BaseModel):
    title:str
    project_id:int
    status:str

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        if value not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")
        return value

class TaskUpdateModel(BaseModel):
    title:Optional[str]=None
    status:Optional[str]=None

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):
        if value not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")
        return value

class TaskResponseModel(BaseModel):
    task_id:int
    task_title:str
    task_status:str
    created_at:datetime
    project_id:int
    of_project:ProjectResponseModel
    class Config:
        orm_mode = True

# class Token(BaseModel):
#     access_token:str
#     token_type:str

class TokenData(BaseModel):
    token_user_id: Optional[int]=None
