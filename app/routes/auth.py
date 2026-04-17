from fastapi import APIRouter

from app.schemas.auth import SignupSchema,loginSchema
from    app.services.auth_services import signup_user, login_user
from app.dependencies.db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.security import create_access_token,create_refresh_token,SECRET_KEY,ALGORITHM
from jose import jwt
from fastapi import HTTPException


router = APIRouter(prefix="/auth",tags=["auth"])

@router.post("/signup")
def signup(data: SignupSchema, db: Session = Depends(get_db)):
    return signup_user(db, data.email, data.password,data.username,data.user_type)

@router.post("/login")
def login(data: loginSchema, db: Session = Depends(get_db)):
    return login_user(db, data.email, data.password)


@router.post("/refresh")
def refresh_token(refresh_token:str):
    try:
        payload = jwt.decode(refresh_token,SECRET_KEY,algorithms=[ALGORITHM])

        if payload.get("type") == "refresh":
            raise HTTPException(status_code=401,detail="Invalid token type")
        user_id = payload.get("sub")

        new_access_token = create_access_token({"user_id": user_id})

        return {"access_token": new_access_token}
    except jwt.JWTError:
        raise HTTPException(status_code=401,detail="Invalid refresh token")
    
        
        