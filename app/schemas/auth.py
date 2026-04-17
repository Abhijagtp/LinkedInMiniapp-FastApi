# Here comes the schema logic  --> shape of data 

from pydantic import BaseModel , EmailStr
from app.models.enums import UserTypeEnum 


class SignupSchema(BaseModel):
    username:str
    email : EmailStr
    password : str
    user_type :UserTypeEnum
    


class loginSchema(BaseModel):
    email : EmailStr
    password : str


